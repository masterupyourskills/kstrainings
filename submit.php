<?php
header('Content-Type: application/json');

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name'] ?? '');
    $email = htmlspecialchars($_POST['email'] ?? '');
    $phone = htmlspecialchars($_POST['phone'] ?? '');
    $course = htmlspecialchars($_POST['course'] ?? '');
    $support_type = htmlspecialchars($_POST['support_type'] ?? '');
    $description = htmlspecialchars($_POST['description'] ?? '');
    $captcha = trim($_POST['captcha'] ?? '');
    
    // Honeypot field (hidden in CSS to catch autobots)
    $bot_check = $_POST['website'] ?? '';
    if (!empty($bot_check)) {
        die(json_encode(["status" => "error", "message" => "Bot detected."]));
    }

    // Basic Math CAPTCHA verification to block automated spam scripts
    if ($captcha !== '7') {
        die(json_encode(["status" => "error", "message" => "CAPTCHA failed. Please enter the correct math answer."]));
    }

    if(empty($name) || empty($email) || empty($phone)) {
        die(json_encode(["status" => "error", "message" => "Missing required fields."]));
    }

    // 1. Save to SQLite Database (Creates table automatically)
    try {
        $db = new PDO('sqlite:database.sqlite');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        
        $db->exec("CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            course TEXT,
            support_type TEXT,
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )");
        
        $stmt = $db->prepare("INSERT INTO submissions (name, email, phone, course, support_type, description) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->execute([$name, $email, $phone, $course, $support_type, $description]);
        
    } catch(Exception $e) {
        // Log DB error but continue to email
        error_log("Database Error: " . $e->getMessage());
    }

    // 2. Send Email Notification
    $to = "info@kstrainings.com";
    $subject = "New Demo/Support Request from $name";
    
    $message = "You have received a new request on kstrainings.com:\n\n";
    $message .= "Name: $name\n";
    $message .= "Email: $email\n";
    $message .= "Phone: $phone\n";
    $message .= "Course: $course\n";
    $message .= "Support Type: $support_type\n";
    $message .= "Requirement Description:\n$description\n";
    
    $headers = "From: no-reply@kstrainings.com\r\n";
    $headers .= "Reply-To: $email\r\n";
    
    // Ensure the mail function works on the web host
    $mail_sent = @mail($to, $subject, $message, $headers);
    
    echo json_encode(["status" => "success", "message" => "Request received successfully! Our team will contact you shortly."]);
} else {
    echo json_encode(["status" => "error", "message" => "Invalid request method."]);
}
?>
