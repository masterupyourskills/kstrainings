import os
import re

# Database of courses with their detailed customizations
courses_db = [   {   'badge': 'Data Analyst',
        'cat': 'data-analyst',
        'desc': 'Master SQL query writing, complex joins, subqueries, database design, indexing, and query '
                'optimization from industry experts. Real-world database scenarios.',
        'faqs': [   {   'a': 'No programming experience is needed. SQL is written in readable English-like syntax, '
                             'making it highly accessible for beginners.',
                        'q': 'Do I need programming experience for SQL?'},
                    {   'a': 'We cover MySQL, PostgreSQL, and MS SQL Server to give you a comprehensive database '
                             'background.',
                        'q': 'Which SQL databases are taught?'},
                    {   'a': 'Yes, we offer 100% confidential on-job support for database design, query writing, and '
                             'data extraction tasks.',
                        'q': 'Is on-job support available for SQL?'}],
        'features': [   {   'desc': 'Write complex SELECT statements, WHERE clauses, and aggregate functions.',
                            'title': 'Basic & Advanced Queries'},
                        {   'desc': 'Master Inner, Left, Right, Full Outer Joins, and nested subqueries.',
                            'title': 'Joins & Subqueries'},
                        {   'desc': 'Learn normalization (1NF, 2NF, 3NF) and entity-relationship models.',
                            'title': 'Database Schema Design'},
                        {   'desc': 'Create indexes, analyze execution plans, and optimize slow queries.',
                            'title': 'Indexes & Performance'},
                        {   'desc': 'Write stored procedures, functions, triggers, and manage views.',
                            'title': 'Stored Procedures & Views'},
                        {   'desc': 'Build and query production-scale relational database schemas.',
                            'title': 'Real-world Capstones'}],
        'filename': 'sql-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 '
                '2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 '
                '2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>',
        'name': 'SQL & Relational Databases',
        'title': 'SQL & Relational Databases Training | Master Database Queries'},
    {   'badge': 'Data Analyst',
        'cat': 'data-analyst',
        'desc': 'Master data cleaning, processing, manipulation, and professional visualization using Python, Pandas, '
                'NumPy, Matplotlib, and Seaborn libraries.',
        'faqs': [   {   'a': 'No, we start from basic Python syntax, data types, and loops before moving to data '
                             'analysis libraries.',
                        'q': 'Is prior Python experience required?'},
                    {   'a': 'Yes, you will analyze real-world datasets from finance, healthcare, e-commerce, and '
                             'marketing.',
                        'q': 'Will I work on real datasets?'}],
        'features': [   {   'desc': 'Master data loading, filtering, grouping, aggregation, and merging.',
                            'title': 'Pandas & DataFrames'},
                        {   'desc': 'Perform fast numerical computations and matrix manipulation.',
                            'title': 'NumPy Computations'},
                        {   'desc': 'Handle missing values, outliers, duplicate records, and data type casting.',
                            'title': 'Data Cleaning & Prep'},
                        {   'desc': 'Create charts with Matplotlib, Seaborn, and interactive Plotly visualizers.',
                            'title': 'Interactive Visualizations'},
                        {   'desc': 'Uncover hidden insights, correlations, and distributions in large datasets.',
                            'title': 'Exploratory Data Analysis (EDA)'},
                        {   'desc': 'Extract data from REST APIs and scrape HTML pages using BeautifulSoup.',
                            'title': 'API & Web Scraping'}],
        'filename': 'python-analyst-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm-1 '
                '15.5v-3.5H9v3.5H7v-3.5H5.5V11H7V7.5h2V11h2v4.5h-2zm6-4.5h-2v4.5h-2V13h-1.5v-2H13V7.5h2V11h2v2z"/></svg>',
        'name': 'Python for Data Analysis',
        'title': 'Python for Data Analysis Training | Master Pandas & NumPy'},
    {   'badge': 'Data Analyst',
        'cat': 'data-analyst',
        'desc': 'Master Power BI Desktop, DAX formulas, Power Query, gateway setups, and publishing to Power BI '
                'Service. Build interactive executive dashboards.',
        'faqs': [   {   'a': 'Yes, this course is fully aligned with the Microsoft Power BI Data Analyst (PL-300) '
                             'certification syllabus.',
                        'q': 'Does this prepare me for the PL-300 exam?'}],
        'features': [   {   'desc': 'Connect to diverse data sources, transform data shapes, and clean data.',
                            'title': 'Power Query ETL'},
                        {   'desc': 'Design star schemas, manage relationships, and handle granularity levels.',
                            'title': 'Data Modeling'},
                        {   'desc': 'Write simple to complex DAX measures, columns, and time-intelligence queries.',
                            'title': 'DAX Formulas'},
                        {   'desc': 'Create advanced charts, maps, custom visuals, and drill-through matrices.',
                            'title': 'Interactive Visuals'},
                        {   'desc': 'Publish reports, schedule automatic refreshes, build workspaces and apps.',
                            'title': 'Power BI Service'},
                        {   'desc': 'Configure enterprise gateways to connect cloud reports to local servers.',
                            'title': 'Gateway Configuration'}],
        'filename': 'powerbi-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/></svg>',
        'name': 'Power BI Certification',
        'title': 'Power BI Certification Training | Data Modeling & DAX Dashboarding'},
    {   'badge': 'Data Analyst',
        'cat': 'data-analyst',
        'desc': 'Master Microsoft Fabric, OneLake, Synapse Data Engineering, Data Factory pipelines, Synapse Data '
                'Warehouse, and Real-Time Analytics.',
        'faqs': [   {   'a': 'Microsoft Fabric is a unified SaaS analytics platform that integrates data factory '
                             'pipelines, Synapse warehouse, data lake, and Power BI into a single dashboard.',
                        'q': 'What is Microsoft Fabric?'}],
        'features': [   {   'desc': "Understand Fabric's single SaaS lake architecture for all data assets.",
                            'title': 'OneLake Architecture'},
                        {   'desc': 'Build enterprise-grade copy pipelines and orchestrate data flows.',
                            'title': 'Fabric Data Factory'},
                        {   'desc': 'Implement Lakehouse designs combining data lake scalability with SQL reliability.',
                            'title': 'Synapse Lakehouse'},
                        {   'desc': 'Store data in open Delta format for seamless analytics and sharing.',
                            'title': 'Delta Lake Storage'},
                        {   'desc': 'Perform high-performance serverless SQL analytics at scale.',
                            'title': 'Synapse Data Warehouse'},
                        {   'desc': 'Build reports that query datasets directly from OneLake without refreshing.',
                            'title': 'Power BI DirectLake'}],
        'filename': 'ms-fabric-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2zm0 4.8L18.6 19H5.4L12 6.8z"/></svg>',
        'name': 'Microsoft Fabric',
        'title': 'Microsoft Fabric Training | Unified SaaS Analytics platform'},
    {   'badge': 'Data Analyst',
        'cat': 'data-analyst',
        'desc': 'Master Tableau dashboards, stories, calculations, level-of-detail (LOD) expressions, parameters, and '
                'Tableau Server administration.',
        'faqs': [   {   'a': 'Tableau is highly favored for visual aesthetics and large dataset mapping, while Power '
                             'BI integrates best with Microsoft ecosystems. We teach both!',
                        'q': 'Tableau vs Power BI - which is better?'}],
        'features': [   {   'desc': 'Build highly interactive, beautiful, and performant visualizations.',
                            'title': 'Dashboard Design'},
                        {   'desc': 'Write Fixed, Include, and Exclude level-of-detail expressions.',
                            'title': 'LOD Calculations'},
                        {   'desc': 'Shape, clean, and combine datasets visually before building reports.',
                            'title': 'Tableau Prep Builder'},
                        {   'desc': 'Plot geospatial data, customize map layers, and perform spatial joins.',
                            'title': 'Mapping & Geospatial'},
                        {   'desc': 'Structure reports as narrative data stories to drive business action.',
                            'title': 'Storytelling with Data'},
                        {   'desc': 'Manage user roles, row-level security, and publication lifecycles.',
                            'title': 'Server Administration'}],
        'filename': 'tableau-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2V5c0-1.1-.9-2-2-2zM9 17H7v-4h2v4zm4 0h-2V7h2v10zm4 0h-2v-9h2v9z"/></svg>',
        'name': 'Tableau Desktop & Server',
        'title': 'Tableau Desktop & Server Training | Advanced Data Visualization'},
    {   'badge': 'Data Analyst',
        'cat': 'data-analyst',
        'desc': 'Master Elasticsearch indexing, query DSL, Logstash data ingestion, Kibana dashboarding, and ELK log '
                'analysis pipelines.',
        'faqs': [   {   'a': 'ELK (Elasticsearch, Logstash, Kibana) is the industry standard for application log '
                             'monitoring, search functions, and security audits.',
                        'q': 'What is the ELK Stack used for?'}],
        'features': [   {   'desc': 'Understand sharding, replicas, mapping, and cluster anatomy.',
                            'title': 'Elasticsearch Indexing'},
                        {   'desc': 'Write complex search queries, term searches, filtering, and aggregation.',
                            'title': 'Query DSL DSL'},
                        {   'desc': 'Collect log and event data, parse with Grok filters, and output to ES.',
                            'title': 'Logstash Pipeline Ingestion'},
                        {   'desc': 'Build search queries, dashboards, and configure alerting metrics.',
                            'title': 'Kibana Visualizations'},
                        {   'desc': 'Install and configure Filebeat, Metricbeat, and Packetbeat log agents.',
                            'title': 'Beats Log Agents'},
                        {   'desc': 'Monitor cluster health, resolve index issues, and scale operations.',
                            'title': 'Cluster Administration'}],
        'filename': 'elasticsearch-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 '
                '9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 '
                '0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>',
        'name': 'Elasticsearch & ELK Stack',
        'title': 'Elasticsearch & ELK Stack Training | Master Logstash & Kibana'},
    {   'badge': 'Data Scientist',
        'cat': 'data-science',
        'desc': 'Master Artificial Neural Networks (ANN), Deep Learning, Convolutional Neural Networks (CNN), '
                'Recurrent Neural Networks (RNN), and Computer Vision.',
        'faqs': [   {   'a': 'We explain linear algebra, probability, and calculus in an intuitive, visual manner as '
                             'we write the code.',
                        'q': 'What mathematics is required for AI?'}],
        'features': [   {   'desc': 'Build and train multi-layer feedforward artificial neural networks (ANN).',
                            'title': 'Deep Learning Models'},
                        {   'desc': 'Implement image classification, object detection using YOLO and OpenCV.',
                            'title': 'Computer Vision (CNN)'},
                        {   'desc': 'Build text classification, sentiment analyzers, and sequence models.',
                            'title': 'Natural Language Processing'},
                        {   'desc': 'Train models using industry-leading deep learning frameworks.',
                            'title': 'PyTorch & TensorFlow'},
                        {   'desc': 'Apply backpropagation optimization, dropout rates, and batch normalization.',
                            'title': 'Hyperparameter Tuning'},
                        {   'desc': 'Containerize models with Docker and serve them via FastAPI endpoints.',
                            'title': 'AI Model Deployment'}],
        'filename': 'ai-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 '
                '9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 '
                '0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 0 1 7 9c0-2.76 2.24-5 5-5s5 2.24 '
                '5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>',
        'name': 'Artificial Intelligence (AI)',
        'title': 'Artificial Intelligence (AI) Course | Deep Learning & neural networks'},
    {   'badge': 'Data Scientist',
        'cat': 'data-science',
        'desc': 'Master regression, classification, clustering algorithms, feature engineering, dimensional reduction, '
                'and ML model evaluation.',
        'faqs': [   {   'a': 'You will master Python, Scikit-Learn, Pandas, NumPy, Jupyter Notebooks, and Anaconda.',
                        'q': 'What tools will I learn?'}],
        'features': [   {   'desc': 'Master Linear & Logistic Regression, Decision Trees, and Random Forests.',
                            'title': 'Supervised Learning'},
                        {   'desc': 'Implement Support Vector Machines (SVM), Naive Bayes, and KNN models.',
                            'title': 'Advanced Classification'},
                        {   'desc': 'Implement K-Means clustering, hierarchical clustering, and DBSCAN.',
                            'title': 'Unsupervised Clustering'},
                        {   'desc': 'Reduce features and compress data sizes using PCA and t-SNE.',
                            'title': 'Dimensionality Reduction'},
                        {   'desc': 'Handle categorical encoders, scale variables, and balance datasets (SMOTE).',
                            'title': 'Feature Engineering'},
                        {   'desc': 'Interpret Confusion Matrix, ROC-AUC curves, Precision, Recall, and F1-score.',
                            'title': 'Model Evaluation Metrics'}],
        'filename': 'ml-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>',
        'name': 'Machine Learning (ML)',
        'title': 'Machine Learning (ML) Course | Supervised & Unsupervised Learning'},
    {   'badge': 'Data Scientist',
        'cat': 'data-science',
        'desc': 'Master Large Language Models (LLMs), prompt engineering, Vector databases, Retrieval-Augmented '
                'Generation (RAG), and model fine-tuning.',
        'faqs': [   {   'a': 'Yes, basic Python knowledge is required to integrate LLMs, build pipelines, and connect '
                             'vector databases.',
                        'q': 'Is coding needed for Generative AI?'}],
        'features': [   {   'desc': 'Connect and query OpenAI GPT-4, Anthropic Claude, and Llama 3 models via APIs.',
                            'title': 'LLM Integration'},
                        {   'desc': 'Store and search text embeddings using Pinecone, ChromaDB, and FAISS.',
                            'title': 'Vector Databases'},
                        {   'desc': 'Build custom knowledge base Q&A chatbots using Retrieval-Augmented Generation.',
                            'title': 'RAG Architectures'},
                        {   'desc': 'Orchestrate complex LLM workflows, document parsing, and indexing pipelines.',
                            'title': 'LangChain & LlamaIndex'},
                        {   'desc': 'Master few-shot learning, chain-of-thought, and system prompt formatting.',
                            'title': 'Prompt Engineering'},
                        {   'desc': 'Apply QLoRA and PEFT to customize open-source LLMs on specific datasets.',
                            'title': 'Fine-Tuning Models'}],
        'filename': 'gen-ai-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 '
                '9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 '
                '0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 0 1 7 9c0-2.76 2.24-5 5-5s5 2.24 '
                '5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>',
        'name': 'Generative AI (GenAI)',
        'title': 'Generative AI (GenAI) Course | Master LLMs, GPT-4 & RAG'},
    {   'badge': 'Data Scientist',
        'cat': 'data-science',
        'desc': 'Master autonomous AI agents, multi-agent orchestrations, LangGraph, CrewAI, AutoGen, tool calling, '
                'and planning architectures.',
        'faqs': [   {   'a': 'Agentic AI refers to LLMs operating as autonomous agents that can plan, use external '
                             'software tools, and collaborate in teams to solve complex goals.',
                        'q': 'What is Agentic AI?'}],
        'features': [   {   'desc': 'Build self-reasoning agents that decide task sequences independently.',
                            'title': 'Autonomous AI Agents'},
                        {   'desc': 'Design collaborative teams of AI agents using CrewAI and AutoGen frameworks.',
                            'title': 'Multi-agent Systems'},
                        {   'desc': 'Implement stateful, cyclical multi-agent workflows using LangGraph.',
                            'title': 'LangGraph Workflows'},
                        {   'desc': 'Equip agents to run SQL queries, browse the web, and call API endpoints.',
                            'title': 'Tool Calling & Binding'},
                        {   'desc': 'Implement short-term and long-term memory architectures for LLM agents.',
                            'title': 'Planning & Memory'},
                        {   'desc': 'Deploy resilient agent loops that recover from errors and API timeouts.',
                            'title': 'Production Deployment'}],
        'filename': 'agentic-ai-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'Agentic AI',
        'title': 'Agentic AI Course | Master LangChain Agents & CrewAI'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master AWS Big Data services, Glue cataloging, Athena serverless SQL, Redshift cloud data '
                'warehousing, EMR Spark clusters, and Kinesis streams.',
        'faqs': [   {   'a': 'Yes, the course covers all objectives for the AWS Certified Data Engineer - Associate '
                             '(DEA-C01) exam.',
                        'q': 'Does this prepare me for the AWS Data Engineer Associate exam?'}],
        'features': [   {   'desc': 'Build automated serverless ETL jobs and discover schemas in S3.',
                            'title': 'Glue ETL & Crawler'},
                        {   'desc': 'Implement scalable MPP cloud data warehouses and database structures.',
                            'title': 'Redshift Warehouse'},
                        {   'desc': 'Query multi-terabyte data directly in S3 using standard SQL scripts.',
                            'title': 'Athena Serverless SQL'},
                        {   'desc': 'Configure Elastic MapReduce clusters to process massive big data workloads.',
                            'title': 'EMR Spark Analytics'},
                        {   'desc': 'Ingest, process, and analyze streaming log and IoT data in real-time.',
                            'title': 'Kinesis Real-Time Streams'},
                        {   'desc': 'Secure data lakes with AWS Lake Formation, KMS encryption, and IAM.',
                            'title': 'Data Pipeline Security'}],
        'filename': 'aws-data-engineer-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 '
                '8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>',
        'name': 'AWS Data Engineering',
        'title': 'AWS Data Engineering Certification | Master AWS Glue & Redshift'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master Azure Data Factory (ADF) pipelines, Azure Databricks Spark clusters, Azure Synapse Analytics, '
                'Gen2 storage, and Stream Analytics.',
        'faqs': [   {   'a': 'Yes, this training is fully mapped to the Microsoft Certified Azure Data Engineer '
                             'Associate (DP-203) exam syllabus.',
                        'q': 'Is this course aligned with DP-203 exam?'}],
        'features': [   {   'desc': 'Orchestrate data ingestion pipelines, activities, and data flows in ADF.',
                            'title': 'Azure Data Factory'},
                        {   'desc': 'Build serverless and dedicated SQL pools for enterprise data warehouses.',
                            'title': 'Synapse Analytics'},
                        {   'desc': 'Run collaborative PySpark notebook scripts on auto-scaling clusters.',
                            'title': 'Azure Databricks Spark'},
                        {   'desc': 'Organize enterprise data lakes using hierarchical namespace directory folders.',
                            'title': 'ADLS Gen2 Storage'},
                        {   'desc': 'Process high-speed event streaming and load targets instantly.',
                            'title': 'Stream Analytics'},
                        {   'desc': 'Apply data catalog classifications, lineage tracing, and access controls.',
                            'title': 'Purview Governance'}],
        'filename': 'azure-data-engineer-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 '
                '8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>',
        'name': 'Azure Data Engineering',
        'title': 'Azure Data Engineering Training | Master Azure Data Factory'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master Google Cloud data warehousing with BigQuery, serverless data pipelines with Dataflow (Apache '
                'Beam), Dataproc clusters, and Composer orchestration.',
        'faqs': [   {   'a': 'Yes, this course covers all exam objectives and case studies.',
                        'q': 'Does this prepare me for Google Professional Data Engineer certification?'}],
        'features': [   {   'desc': 'Optimize tables with clustering, partitioning, and serverless SQL.',
                            'title': 'BigQuery Data Warehouse'},
                        {   'desc': 'Build unified batch and stream processing pipelines with serverless Dataflow.',
                            'title': 'Dataflow Apache Beam'},
                        {   'desc': 'Migrate Hadoop and Spark workloads to GCP using managed Dataproc.',
                            'title': 'Dataproc Managed Spark'},
                        {   'desc': 'Orchestrate complex workflow DAGs using managed Apache Airflow.',
                            'title': 'Cloud Composer Airflow'},
                        {   'desc': 'Ingest scalable real-time streaming data from diverse endpoints.',
                            'title': 'Pub/Sub Messaging'},
                        {   'desc': 'Design wide-column database tables for fast low-latency data access.',
                            'title': 'Bigtable NoSQL Database'}],
        'filename': 'gcp-data-engineer-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2z"/></svg>',
        'name': 'GCP Data Engineering',
        'title': 'GCP Data Engineering Training | Master BigQuery & Dataflow'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master the Databricks Lakehouse Platform, Delta Lake storage tables, Unity Catalog governance, '
                'PySpark processing, and Databricks SQL.',
        'faqs': [   {   'a': 'A Lakehouse is a modern data platform architecture that combines the cost-effective '
                             'storage of data lakes with the data management of data warehouses.',
                        'q': 'What is a Databricks Lakehouse?'}],
        'features': [   {   'desc': 'Implement ACID transactions, time travel, and schema enforcement on Delta tables.',
                            'title': 'Delta Lake Storage'},
                        {   'desc': 'Build clean data pipelines using Bronze, Silver, and Gold delta layers.',
                            'title': 'Medallion Architecture'},
                        {   'desc': 'Manage secure data access controls, lineage, and discovery across workspace '
                                    'tables.',
                            'title': 'Unity Catalog Governance'},
                        {   'desc': 'Write scalable data transformations inside collaborative notebook environments.',
                            'title': 'PySpark Integration'},
                        {   'desc': 'Build declarative, auto-scaling pipeline structures with built-in quality checks.',
                            'title': 'Delta Live Tables (DLT)'},
                        {   'desc': 'Run low-latency business intelligence queries directly on Lakehouse files.',
                            'title': 'Databricks SQL Analytics'}],
        'filename': 'databricks-data-engineer-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2zm0 4.8L18.6 19H5.4L12 6.8z"/></svg>',
        'name': 'Databricks Data Engineering',
        'title': 'Databricks Data Engineering Training | Delta Lake & Unity Catalog'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master Apache Spark architecture, PySpark DataFrames, Spark SQL, structured streaming, cluster '
                'tuning, and big data transformations.',
        'faqs': [   {   'a': 'No, PySpark allows you to write Spark code in Python, which is now the most popular '
                             'language for data engineering.',
                        'q': 'Do I need Scala to learn Spark?'}],
        'features': [   {   'desc': 'Understand Driver, Executors, RDDs, Lineage, and lazy evaluation designs.',
                            'title': 'Spark Core Architecture'},
                        {   'desc': 'Write scalable data transformations, filtering, aggregation, and grouping.',
                            'title': 'PySpark DataFrames API'},
                        {   'desc': 'Query big data files using ANSI-compliant SQL scripts inside Spark tables.',
                            'title': 'Spark SQL Engine'},
                        {   'desc': 'Master caching, partitioning, partitioning strategies, and broad-joins.',
                            'title': 'Performance Optimization'},
                        {   'desc': 'Build real-time streaming data pipelines with sliding windows and watermarks.',
                            'title': 'Structured Streaming'},
                        {   'desc': 'Deploy Spark jobs on Standalone, YARN, and Kubernetes cluster engines.',
                            'title': 'Cluster Deployment'}],
        'filename': 'pyspark-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'Apache Spark & PySpark',
        'title': 'Apache Spark & PySpark Training | Big Data Transformation'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master Snowflake architecture, virtual warehouses, zero-copy cloning, time travel, secure data '
                'sharing, and Snowpipe automated loading.',
        'faqs': [   {   'a': 'Yes, our curriculum fully covers all topics tested in the official SnowPro Core '
                             'certification.',
                        'q': 'Does this prepare me for SnowPro Core certification?'}],
        'features': [   {   'desc': 'Scale compute warehouses and databases independently without bottlenecks.',
                            'title': 'Separated Storage & Compute'},
                        {   'desc': 'Clone multi-terabyte databases instantly for testing with zero extra storage '
                                    'cost.',
                            'title': 'Zero-Copy Cloning'},
                        {   'desc': 'Query, restore, and recover deleted data assets from up to 90 days ago.',
                            'title': 'Snowflake Time Travel'},
                        {   'desc': 'Build automated, continuous file loading pipelines from AWS S3 or Azure ADLS.',
                            'title': 'Snowpipe ETL Loader'},
                        {   'desc': 'Share live database tables securely with external clients without copying data.',
                            'title': 'Data Sharing & Marketplace'},
                        {   'desc': 'Ingest and query JSON, Parquet, and XML datasets natively using SQL Variant.',
                            'title': 'Semi-Structured Formats'}],
        'filename': 'snowflake-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2V5c0-1.1-.9-2-2-2z"/></svg>',
        'name': 'Snowflake Cloud Data Warehouse',
        'title': 'Snowflake Cloud Data Warehouse Training | Master Snowpipe'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master MySQL database design, transaction management, indexing, stored procedures, replication '
                'setups, and performance tuning.',
        'faqs': [   {   'a': "Yes, MySQL is the world's most popular open-source relational database, powering "
                             'millions of production applications.',
                        'q': 'Is MySQL still relevant in big data?'}],
        'features': [   {   'desc': 'Design normalized tables, primary/foreign keys, and constraints.',
                            'title': 'Relational Modeling'},
                        {   'desc': 'Write secure database transactions with COMMIT, ROLLBACK, and isolation levels.',
                            'title': 'Transaction Control (ACID)'},
                        {   'desc': 'Master database manipulation queries, joining datasets, and group tables.',
                            'title': 'SQL Functions & Joins'},
                        {   'desc': 'Write reusable procedures, conditional loops, cursors, and triggers.',
                            'title': 'Stored Procedures'},
                        {   'desc': 'Interpret EXPLAIN plans, configure slow query logs, and optimize database '
                                    'indexes.',
                            'title': 'Query Performance Tuning'},
                        {   'desc': 'Set up database replication, binary logs, backups, and recovery strategies.',
                            'title': 'Master-Slave Replication'}],
        'filename': 'mysql-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93z"/></svg>',
        'name': 'MySQL Developer & DBA',
        'title': 'MySQL Developer & DBA Training | Relational Database Management'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master Oracle PL/SQL programming, packages, cursors, triggers, exception handling, dynamic SQL, and '
                'database query optimization.',
        'faqs': [   {   'a': "SQL is a declarative language to query databases, whereas PL/SQL is Oracle's procedural "
                             'extension allowing loops, variables, and logic.',
                        'q': 'What is the difference between SQL and PL/SQL?'}],
        'features': [   {   'desc': 'Understand declarations, execution blocks, loops, and conditional structures.',
                            'title': 'PL/SQL Block Structure'},
                        {   'desc': 'Manage result sets row-by-row using cursors, parameterized loops, and record '
                                    'bulk-collects.',
                            'title': 'Explicit & Implicit Cursors'},
                        {   'desc': 'Build modular code with package specifications and body declarations.',
                            'title': 'PL/SQL Packages'},
                        {   'desc': 'Implement row-level and statement-level triggers to enforce business rules '
                                    'automatically.',
                            'title': 'Database Triggers'},
                        {   'desc': 'Master nested tables, associative arrays, varrays, and BULK COLLECT logic.',
                            'title': 'Advanced collections'},
                        {   'desc': 'Execute dynamic SQL statements at runtime using EXECUTE IMMEDIATE queries.',
                            'title': 'Dynamic SQL Execution'}],
        'filename': 'oracle-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93z"/></svg>',
        'name': 'Oracle PL/SQL Developer',
        'title': 'Oracle PL/SQL Developer Training | Master Advanced PL-SQL'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master MS SQL Server querying, T-SQL scripting, SSIS package development, data warehouse loading, and '
                'SQL Server DBA administration.',
        'faqs': [   {   'a': 'SSIS (SQL Server Integration Services) is an enterprise ETL tool used to extract, '
                             'transform, and load data from diverse sources into SQL Server.',
                        'q': 'What is SSIS?'}],
        'features': [   {   'desc': 'Write SQL queries, CTEs, Window Functions, and subqueries on SQL Server.',
                            'title': 'T-SQL Query Scripting'},
                        {   'desc': 'Build Integration Services packages, data transformations, and loops.',
                            'title': 'SSIS ETL Packages'},
                        {   'desc': 'Implement robust backend query logic with transaction parameters.',
                            'title': 'Stored Procedures & UDFs'},
                        {   'desc': 'Automate database backups, database integrity checks, and execute SSIS jobs.',
                            'title': 'SQL Server Agent Jobs'},
                        {   'desc': 'Configure clustered and non-clustered indexes to optimize slow queries.',
                            'title': 'Database Indexing'},
                        {   'desc': 'Deploy packages to the SSISDB catalog catalog and monitor executions.',
                            'title': 'SSIS Deployment'}],
        'filename': 'ms-sql-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2v14h-2z"/></svg>',
        'name': 'Microsoft SQL Server & SSIS',
        'title': 'Microsoft SQL Server & SSIS Training | Master ETL Pipelines'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master Apache Airflow DAGs, custom operators, schedulers, execution executors, pipeline monitoring, '
                'and deployment on Kubernetes.',
        'faqs': [   {   'a': 'Airflow is the industry standard workflow orchestrator to schedule and monitor complex '
                             'data workflows, databases, and machine learning pipelines.',
                        'q': 'What is Airflow used for?'}],
        'features': [   {   'desc': 'Write data pipeline pipelines as Directed Acyclic Graphs (DAGs) in Python code.',
                            'title': 'DAG Programming'},
                        {   'desc': 'Master BashOperator, PythonOperator, EmailOperator, and custom hooks.',
                            'title': 'Airflow Operators'},
                        {   'desc': 'Define complex upstream and downstream flows with branching operators.',
                            'title': 'Task Dependencies'},
                        {   'desc': 'Understand Schedulers, Web Servers, Workers, and Celery / Kubernetes executors.',
                            'title': 'Airflow Scheduler & Execs'},
                        {   'desc': 'Manage execution dates, task parameters, macros, and connection vaults safely.',
                            'title': 'Task Context & Variables'},
                        {   'desc': 'Configure real-time pipeline failure alerts to Slack, email, or webhook hooks.',
                            'title': 'Monitoring & SLA Alerts'}],
        'filename': 'airflow-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'Apache Airflow In Production',
        'title': 'Apache Airflow In Production Training | Orchestrate Data Pipelines'},
    {   'badge': 'Data Engineer',
        'cat': 'data-engineer',
        'desc': 'Master Python programming for database operations, ETL pipeline design, data serialization (Parquet, '
                'JSON), API integrations, and log parsing.',
        'faqs': [   {   'a': 'Data engineers write Python scripts to automate files parsing, fetch data from web '
                             'endpoints, perform schema validations, and orchestrate tools.',
                        'q': 'How is Python used in Data Engineering?'}],
        'features': [   {   'desc': 'Write custom Python scripts to extract, transform, and load files into targets.',
                            'title': 'ETL Pipeline Pipelines'},
                        {   'desc': 'Connect to databases, execute queries, and manage transaction parameters safely.',
                            'title': 'DB Integrations (SQLAlchemy)'},
                        {   'desc': 'Read, process, and write Parquet, Avro, JSON, CSV, and XML big data files.',
                            'title': 'File Format Parsers'},
                        {   'desc': 'Request data from external HTTP APIs with paginations and error handlers.',
                            'title': 'REST API Data Ingestion'},
                        {   'desc': 'Speed up CPU-heavy tasks using multiprocessing and concurrency modules.',
                            'title': 'Multiprocessing & Scaling'},
                        {   'desc': 'Track pipeline executions, log run statistics, and handle network drops '
                                    'gracefully.',
                            'title': 'Logging & Error Vaults'}],
        'filename': 'python-data-engineer-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm-1 '
                '15.5v-3.5H9v3.5H7v-3.5H5.5V11H7V7.5h2V11h2v4.5h-2zm6-4.5h-2v4.5h-2V13h-1.5v-2H13V7.5h2V11h2v2z"/></svg>',
        'name': 'Python for Data Engineering',
        'title': 'Python for Data Engineering Training | Build ETL Pipelines'},
    {   'badge': 'Video Editor',
        'cat': 'video-editing',
        'desc': 'Master professional video editing, timeline operations, transitions, audio mixing, color correction '
                '(Lumetri), and export configurations.',
        'faqs': [   {   'a': 'We recommend at least 16GB RAM, an Intel i5/i7 processor, and a dedicated GPU '
                             '(Nvidia/AMD) for smooth rendering.',
                        'q': 'What computer specs do I need?'}],
        'features': [   {   'desc': 'Master ripple edit, rolling edit, slip, slide, and track selection tools.',
                            'title': 'Timeline Editing Tools'},
                        {   'desc': 'Clean background noise, adjust gain levels, and mix background audio tracks.',
                            'title': 'Audio Enhancement & Mixing'},
                        {   'desc': 'Color correct raw footage, match shots, apply LUTs, and color grade clips.',
                            'title': 'Lumetri Color Grading'},
                        {   'desc': 'Apply smooth transitions, keyframe animation effects, and crop clips.',
                            'title': 'Transitions & FX Controls'},
                        {   'desc': 'Build lower thirds, titles, text overlays, and responsive animations.',
                            'title': 'Text & Essential Graphics'},
                        {   'desc': 'Optimize output settings for YouTube, Instagram Reels, or broadcast TV.',
                            'title': 'Export Render Presets'}],
        'filename': 'premiere-pro-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M4 4h16v16H4V4zm4 4v8h2v-3h2v3h2V8H8zm6 0v5h2V8h-2z"/></svg>',
        'name': 'Adobe Premiere Pro',
        'title': 'Adobe Premiere Pro Course | Master Video Editing & Grading'},
    {   'badge': 'Video Editor',
        'cat': 'video-editing',
        'desc': 'Master Final Cut Pro X, the magnetic timeline, multicam editing, color grading, motion graphics, and '
                'high-speed rendering on macOS.',
        'faqs': [   {   'a': 'No, Final Cut Pro is exclusive to Apple macOS. You must have a Mac (MacBook, iMac, or '
                             'Mac Mini) to follow this course.',
                        'q': 'Does FCP run on Windows?'}],
        'features': [   {   'desc': 'Edit clips dynamically without losing audio sync or leaving empty track gaps.',
                            'title': 'Magnetic Timeline'},
                        {   'desc': 'Sync and edit footage from up to 64 camera angles simultaneously.',
                            'title': 'Multicam Editing'},
                        {   'desc': 'Color correct clips using color wheels, curves, and advanced keying tools.',
                            'title': 'Advanced Color Board'},
                        {   'desc': 'Import and customize advanced titles, transitions, and generator effects.',
                            'title': 'Apple Motion Templates'},
                        {   'desc': 'Export high-resolution ProRes files and batch render formats fast.',
                            'title': 'Compressor Export Rendering'},
                        {   'desc': 'Organize media assets using keyword collections and smart folders.',
                            'title': 'Library Media Hub'}],
        'filename': 'final-cut-pro-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>',
        'name': 'Apple Final Cut Pro',
        'title': 'Apple Final Cut Pro Course | Magnetic Timeline Editing'},
    {   'badge': 'Video Editor',
        'cat': 'video-editing',
        'desc': "Master DaVinci Resolve's professional editing tools, the industry standard Color Page nodes, "
                'Fairlight audio design, and Fusion VFX.',
        'faqs': [   {   'a': 'Yes! The free version contains 95% of the features needed for professional editing. We '
                             'teach using both Free and Studio versions.',
                        'q': 'Is the free version of DaVinci Resolve enough?'}],
        'features': [   {   'desc': 'Master primary wheels, curves, qualifiers, trackers, and parallel nodes.',
                            'title': 'Node-based Color Page'},
                        {   'desc': 'Perform lightning-fast trimming, inserts, and source tape reviews.',
                            'title': 'Cut & Edit Timelines'},
                        {   'desc': 'Build 3D titles, compositing visual effects, and green screen keys.',
                            'title': 'Fusion VFX workspace'},
                        {   'desc': 'Mix, EQ, compress, and apply noise reductions to professional audio tracks.',
                            'title': 'Fairlight Audio Page'},
                        {   'desc': 'Format HDR grading curves and output video master deliverables.',
                            'title': 'HDR Color Grading'},
                        {   'desc': 'Optimize encoding parameters for streaming platforms or cinema projectors.',
                            'title': 'Deliver Preset Encoding'}],
        'filename': 'davinci-resolve-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 22c5.52 0 10-4.48 10-10S17.52 2 12 2 2 6.48 2 12s4.48 10 10 '
                '10zM10.5 7.5L16 12l-5.5 4.5v-9z"/></svg>',
        'name': 'DaVinci Resolve',
        'title': 'DaVinci Resolve Course | Color Grading & Fairlight Audio'},
    {   'badge': 'Video Editor',
        'cat': 'video-editing',
        'desc': 'Master After Effects layer compositions, keyframe animations, masking, tracking, text expressions, '
                'rotoscoping, and 2D/3D VFX.',
        'faqs': [   {   'a': 'No, After Effects is designed for motion graphics, animations, and visual effects. For '
                             'timeline editing, Premiere Pro is preferred.',
                        'q': 'Is After Effects used for regular video editing?'}],
        'features': [   {   'desc': 'Master easing, graph editor velocity handles, and motion paths.',
                            'title': 'Keyframe Animation'},
                        {   'desc': 'Track shapes, cut elements, and rotoscop background subjects.',
                            'title': 'Masking & Rotoscoping'},
                        {   'desc': 'Animate typography using text animators and kinetic presets.',
                            'title': 'Text & Logo Animation'},
                        {   'desc': 'Match moving elements inside raw footage and overlay 3D elements.',
                            'title': '3D Camera Tracker'},
                        {   'desc': 'Automate animation cycles using simple JavaScript-based expressions.',
                            'title': 'Expressions & Rigging'},
                        {   'desc': 'Build particle fields, atmospheric effects, glow elements, and light flares.',
                            'title': 'VFX & Particle Systems'}],
        'filename': 'after-effects-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M4 4h16v16H4V4zm4 4v8h2v-3h2v3h2V8H8zm6 0v5h2V8h-2z"/></svg>',
        'name': 'Adobe After Effects',
        'title': 'Adobe After Effects Course | Motion Graphics & Animation'},
    {   'badge': 'Video Editor',
        'cat': 'video-editing',
        'desc': 'Learn Wondershare Filmora to quickly edit social media videos, apply presets, adjust audio, add '
                'transitions, and export files.',
        'faqs': [   {   'a': 'Yes! Filmora is one of the easiest video editing tools to learn, making it perfect for '
                             'content creators starting out.',
                        'q': 'Is Filmora suitable for beginners?'}],
        'features': [   {   'desc': 'Learn how to import files, cut, trim, join, and align footage.',
                            'title': 'Timeline Basics'},
                        {   'desc': 'Apply ready-made color filters, overlays, and slow-motion settings.',
                            'title': 'Visual Effect Presets'},
                        {   'desc': 'Create callouts, openers, lower thirds, and credit sequences.',
                            'title': 'Text & Titles Templates'},
                        {   'desc': 'Animate multiple videos side-by-side using screen split templates.',
                            'title': 'Split Screen Collages'},
                        {   'desc': 'Add copyright-free music tracks and fade music under spoken vocals.',
                            'title': 'Audio Library & Ducking'},
                        {   'desc': 'Format aspect ratios for YouTube horizontal or TikTok vertical feeds.',
                            'title': 'Direct Social Export'}],
        'filename': 'filmora-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zM10 16.5v-9l6 4.5-6 4.5z"/></svg>',
        'name': 'Wondershare Filmora',
        'title': 'Wondershare Filmora Course | Quick & Social Video Editing'},
    {   'badge': 'Video Editor',
        'cat': 'video-editing',
        'desc': 'Learn Avid Media Composer, the industry standard for Hollywood feature films and television broadcast '
                'editing. Master workflows.',
        'faqs': [   {   'a': "Avid's media database management and collaborative bin-locking make it unmatched for "
                             'organizing massive feature-film datasets.',
                        'q': 'Why is Avid used in Hollywood?'}],
        'features': [   {   'desc': 'Import and link high-resolution offline files to projects safely.',
                            'title': 'Avid AMA Workflows'},
                        {   'desc': 'Understand folder hierarchies, bin organizations, and indexing.',
                            'title': 'Media Database Management'},
                        {   'desc': 'Perform three-point edits and fine-tune trim offsets dynamically.',
                            'title': 'Precision Source Editing'},
                        {   'desc': 'Configure bin locks for multiple editors working on the same project.',
                            'title': 'Collaborative Shared Storage'},
                        {   'desc': 'Relink low-res offline edits to high-res online master files.',
                            'title': 'Conforming & Relinking'},
                        {   'desc': 'Export AAF files for colorists and sound mixers, and render masters.',
                            'title': 'Broadcast Master Deliveries'}],
        'filename': 'avid-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm-1 15.5v-11h3l2 4 2-4h3v11h-3v-6l-2 4h-2l-2-4v6h-3z"/></svg>',
        'name': 'Avid Media Composer',
        'title': 'Avid Media Composer Course | Broadcast Video Editing'},
    {   'badge': 'Photo Editor',
        'cat': 'photo-editing',
        'desc': 'Master Adobe Photoshop, layered compositing, masks, selections, color adjustments, portrait '
                'retouching, and graphic design assets.',
        'faqs': [   {   'a': 'While you can, modern UI/UX designers prefer Figma. Photoshop is best suited for image '
                             'editing and compositing.',
                        'q': 'Can I use Photoshop for UI design?'}],
        'features': [   {   'desc': 'Master layer adjustments, smart objects, and grouping organization.',
                            'title': 'Layers & Non-Destructive'},
                        {   'desc': 'Isolate complex subjects, refine hair lines, and manage channels.',
                            'title': 'Advanced Selection Tools'},
                        {   'desc': 'Blend multiple images seamlessly using mask opacity curves.',
                            'title': 'Layer Mask Compositing'},
                        {   'desc': 'Master clone stamp, healing brushes, content-aware fills, and liquefy.',
                            'title': 'Retouching & Repair'},
                        {   'desc': 'Color match composite layers, isolate highlights, and apply camera raw.',
                            'title': 'Color Grading & Curves'},
                        {   'desc': 'Draw vector paths, custom shapes, and format advanced text blocks.',
                            'title': 'Vector Pen Graphics'}],
        'filename': 'photoshop-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2V5c0-1.1-.9-2-2-2zM8.5 16v-8H11v3h2v-3h2.5v8H8.5z"/></svg>',
        'name': 'Adobe Photoshop',
        'title': 'Adobe Photoshop Course | Advanced Image Editing & Retouching'},
    {   'badge': 'Photo Editor',
        'cat': 'photo-editing',
        'desc': 'Learn Adobe Lightroom Classic, RAW photo processing, library catalog organization, color grading '
                'presets, and batch editing workflows.',
        'faqs': [   {   'a': 'Lightroom is designed for batch processing, organizing, and color grading RAW files, '
                             'while Photoshop is for detailed object removal and compositing.',
                        'q': 'What is the difference between Photoshop and Lightroom?'}],
        'features': [   {   'desc': 'Recover highlights, lift shadow detail, and manage white balance profiles.',
                            'title': 'RAW Development'},
                        {   'desc': 'Apply detailed color grades to shadows, midtones, and highlights.',
                            'title': 'Color Grading Wheels'},
                        {   'desc': 'Target individual color channels to tweak skin tones or sky blues.',
                            'title': 'Hues, Saturation & Luminance'},
                        {   'desc': 'Apply selective adjustments using linear, radial, and brush masks.',
                            'title': 'Masking & Gradients'},
                        {   'desc': 'Build custom color presets and apply changes to hundreds of photos at once.',
                            'title': 'Preset Creation & Batch'},
                        {   'desc': 'Import, tag, flag, star-rate, and filter thousands of photo files.',
                            'title': 'Library cataloging'}],
        'filename': 'lightroom-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2V5c0-1.1-.9-2-2-2zM9 16.5V7.5h2v7.5H9zm7 0h-2V7.5h2v9z"/></svg>',
        'name': 'Adobe Lightroom',
        'title': 'Adobe Lightroom Course | RAW Image Processing & Color'},
    {   'badge': 'Photo Editor',
        'cat': 'photo-editing',
        'desc': 'Learn image manipulation, layer operations, basic compositing, selections, and photo editing using '
                'GIMP, the free open-source editor.',
        'faqs': [   {   'a': 'Yes! GIMP is an open-source, community-driven photo editor that is completely free to '
                             'download and use for personal or commercial work.',
                        'q': 'Is GIMP completely free?'}],
        'features': [   {   'desc': 'Configure panels, tools, single-window layouts, and key bindings.',
                            'title': 'GIMP Workspace & Interface'},
                        {   'desc': 'Work with layers, mask channels, and blend layer outputs.',
                            'title': 'Layer Operations & Modes'},
                        {   'desc': 'Master fuzzy select, color select, paths tool, and extract items.',
                            'title': 'Selection Tools & Extraction'},
                        {   'desc': 'Adjust histograms, levels, curves, saturation, and contrast values.',
                            'title': 'Color Correction & Levels'},
                        {   'desc': 'Use clone tool, healing brush, perspective clone, and blur brushes.',
                            'title': 'Retouching Tools'},
                        {   'desc': 'Configure JPEG, PNG, TIFF, and native XCF project save files.',
                            'title': 'Export Render Formats'}],
        'filename': 'gimp-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2z"/></svg>',
        'name': 'GIMP Photo Editor',
        'title': 'GIMP Photo Editor Course | Open Source Image Editing'},
    {   'badge': 'Photo Editor',
        'cat': 'photo-editing',
        'desc': 'Master Canva Pro, custom brand kits, social media templates, kinetic presentations, PDF layouts, and '
                'video animations.',
        'faqs': [   {   'a': 'No, 90% of the lessons are fully applicable to the free Canva version. We cover Pro '
                             'features as bonus modules.',
                        'q': 'Do I need Canva Pro to follow this course?'}],
        'features': [   {   'desc': 'Navigate layouts, find assets, and import custom files.',
                            'title': 'Canva Workspace Basics'},
                        {   'desc': 'Upload logo assets, set brand colors, and save typography presets.',
                            'title': 'Custom Brand Kits'},
                        {   'desc': 'Design templates for Instagram posts, stories, reels, and YouTube banners.',
                            'title': 'Social Media Graphics'},
                        {   'desc': 'Create business slide decks, proposal documents, and print layouts.',
                            'title': 'Presentations & PDFs'},
                        {   'desc': 'Apply page transitions, animated text, and produce short marketing clips.',
                            'title': 'Animated Assets'},
                        {   'desc': 'Collaborate with clients, leave design feedback, and lock template sections.',
                            'title': 'Team Workspaces'}],
        'filename': 'canva-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 '
                '2-2V5c0-1.1-.9-2-2-2zm-2 10h-2v4.5h-2V13h-1.5v-2H13V7.5h2V11h2v2z"/></svg>',
        'name': 'Canva Graphic Design',
        'title': 'Canva Graphic Design Course | Build Social & Marketing Assets'},
    {   'badge': 'Photo Editor',
        'cat': 'photo-editing',
        'desc': 'Master CorelDraw, vector design paths, branding, logo designs, page formatting, layouts, print '
                'setups, and typography.',
        'faqs': [   {   'a': 'CorelDraw is primarily used for vector print layout, sign-making, and logo design, '
                             'rather than interactive web prototypes.',
                        'q': 'Is CorelDraw used for web design?'}],
        'features': [   {   'desc': 'Master pen, bezier, freehand, and artistic media tools.',
                            'title': 'Vector Drawing Tools'},
                        {   'desc': 'Build scalable vector logo assets, corporate guidelines, and marks.',
                            'title': 'Branding & Logo Designs'},
                        {   'desc': 'Format brochures, menus, business cards, and print templates.',
                            'title': 'Advanced Page Layouts'},
                        {   'desc': 'Work with CMYK profiles for printing and RGB profiles for web files.',
                            'title': 'Color Management'},
                        {   'desc': 'Format artistic text boxes, paragraph containers, and fit text to paths.',
                            'title': 'Typographic Layouts'},
                        {   'desc': 'Apply bleed guidelines, trim marks, color separation, and export PDF master '
                                    'files.',
                            'title': 'Print Prepress Setups'}],
        'filename': 'coreldraw-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2zm0 4.8L18.6 19H5.4L12 6.8z"/></svg>',
        'name': 'CorelDraw Vector Graphics',
        'title': 'CorelDraw Vector Graphics Course | Master Vector Illustration'},
    {   'badge': 'Photo Editor',
        'cat': 'photo-editing',
        'desc': 'Master Figma auto-layout, component libraries, design systems, interactive prototypes, variables, and '
                'developer handoffs.',
        'faqs': [   {   'a': 'Figma is the industry-leading tool to design user interfaces (UI) and user experiences '
                             '(UX) for mobile apps and websites.',
                        'q': 'What is Figma used for?'}],
        'features': [   {   'desc': 'Build responsive, scalable card structures, menu bars, and grids.',
                            'title': 'Auto-Layout Engine'},
                        {   'desc': 'Create master components, nested states, and style variants (button sizes).',
                            'title': 'Component Libraries'},
                        {   'desc': 'Build smart-animated page transitions, slide menus, and custom overlays.',
                            'title': 'Interactive Prototyping'},
                        {   'desc': 'Define shared typography scales, color palettes, grids, and border weights.',
                            'title': 'Design Systems'},
                        {   'desc': 'Apply variables for light/dark modes, padding values, and basic logic.',
                            'title': 'Figma Variables & Logic'},
                        {   'desc': 'Label assets, export formats, read CSS parameters, and inspect code.',
                            'title': 'Developer Handoff Workflows'}],
        'filename': 'figma-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 '
                '10-10-4.48-10-10-10zm-1.5 6c.83 0 1.5.67 1.5 1.5S11.33 11 10.5 11 9 10.33 9 9.5z"/></svg>',
        'name': 'Figma UI/UX Design',
        'title': 'Figma UI/UX Design Course | Master UI Prototyping'},
    {   'badge': 'Web Developer',
        'cat': 'dev',
        'desc': 'Master Java programming, Object-Oriented Principles (OOP), Spring Boot backend APIs, Hibernate/JPA '
                'repositories, and React/Angular frontend integrations.',
        'faqs': [   {   'a': 'Yes! You will build a complete, production-ready Full-Stack E-commerce or Banking '
                             'application from scratch.',
                        'q': 'Do I get a project to build?'}],
        'features': [   {   'desc': 'Master classes, inheritance, interfaces, polymorphism, collections, and streams.',
                            'title': 'Core Java & OOP'},
                        {   'desc': 'Build RESTful API endpoints, handle requests, and validate parameters.',
                            'title': 'Spring Boot APIs'},
                        {   'desc': 'Map Java entities to relational database tables and write clean queries.',
                            'title': 'Spring Data JPA & Hibernate'},
                        {   'desc': 'Secure endpoints with role-based authorization rules and token logins.',
                            'title': 'Spring Security & JWT'},
                        {   'desc': 'Connect Spring Boot backends to React/Angular frontend single-page apps.',
                            'title': 'Frontend Integrations'},
                        {   'desc': 'Build distributed services using Eureka Registry, Gateway, and Feign.',
                            'title': 'Microservices Design'}],
        'filename': 'java-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2z"/></svg>',
        'name': 'Java Full-Stack Developer',
        'title': 'Java Full-Stack Developer Course | Master Spring Boot & React'},
    {   'badge': 'Web Developer',
        'cat': 'dev',
        'desc': 'Master Python programming for the web, Django framework layouts, templates, database integration, '
                'Django REST Framework (DRF), and FastAPI.',
        'faqs': [   {   'a': "Django is Python's most popular web framework, powering major platforms like Instagram, "
                             "Pinterest, and Disqus due to its 'batteries-included' philosophy.",
                        'q': 'Why learn Django?'}],
        'features': [   {   'desc': 'Build views, templates, model databases, and render HTML template files.',
                            'title': 'Django MVT Architecture'},
                        {   'desc': 'Manage database models, run migrations, and write clean database queries.',
                            'title': 'Django ORM Database'},
                        {   'desc': 'Build JSON API endpoints using Django REST Framework (DRF).',
                            'title': 'REST API Development'},
                        {   'desc': 'Write high-performance asynchronous API endpoints using FastAPI and Pydantic.',
                            'title': 'FastAPI Web Framework'},
                        {   'desc': 'Configure user registries, login modules, session states, and JWT logs.',
                            'title': 'User Authentication Vaults'},
                        {   'desc': 'Deploy Python web apps to AWS or Heroku servers using Gunicorn and Nginx.',
                            'title': 'Deployment Engine'}],
        'filename': 'python-web-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2z"/></svg>',
        'name': 'Python Web Dev (Django)',
        'title': 'Python Web Developer Course | Master Django & FastAPI'},
    {   'badge': 'Web Developer',
        'cat': 'dev',
        'desc': 'Master Angular components, templates, TypeScript models, services, RxJS reactive programming, forms, '
                'routing, and state management.',
        'faqs': [   {   'a': 'Yes, Angular is a robust, Google-backed framework favored by major banks and enterprises '
                             'due to its strict structural standard.',
                        'q': 'Is Angular good for enterprise applications?'}],
        'features': [   {   'desc': 'Write clean, type-safe Angular code using TypeScript classes and modules.',
                            'title': 'TypeScript Programming'},
                        {   'desc': 'Build reusable, nested UI components with detailed input/output bindings.',
                            'title': 'Component Architectures'},
                        {   'desc': 'Master reactive programming streams, data subscriptions, and custom operators.',
                            'title': 'RxJS Observables'},
                        {   'desc': 'Configure client-side navigation menus, child views, and navigation guards.',
                            'title': 'Angular Router Modules'},
                        {   'desc': 'Build complex data entry forms with custom validation rules at runtime.',
                            'title': 'Reactive Forms Validation'},
                        {   'desc': 'Manage global app state variables using NgRx stores, actions, and effects.',
                            'title': 'State Management (NgRx)'}],
        'filename': 'angular-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2L2 5v14l10 3 10-3V5L12 2z"/></svg>',
        'name': 'Angular Framework',
        'title': 'Angular Framework Course | Master TypeScript & SPA Design'},
    {   'badge': 'Web Developer',
        'cat': 'dev',
        'desc': 'Master web interface layouts, HTML5 tags, CSS3 responsive grid models, Flexbox, JavaScript '
                'programming, DOM operations, and CSS animations.',
        'faqs': [   {   'a': 'Yes, this is our most popular entry-level course. It requires no prior technical '
                             'experience.',
                        'q': 'Is this suitable for absolute beginners?'}],
        'features': [   {   'desc': 'Write SEO-friendly, semantic, and highly accessible HTML markup layouts.',
                            'title': 'HTML5 Semantic Tags'},
                        {   'desc': 'Build responsive, multi-device page grids without frameworks.',
                            'title': 'CSS3 Flexbox & Grids'},
                        {   'desc': 'Create interactive pages, toggle menus, and validate input fields.',
                            'title': 'JavaScript DOM Controls'},
                        {   'desc': 'Master array operations, async-await calls, classes, and variables.',
                            'title': 'Modern JavaScript (ES6+)'},
                        {   'desc': 'Configure CSS media query rules to format pages for mobile and desktop screens.',
                            'title': 'Responsive Web Design'},
                        {   'desc': 'Implement premium micro-animations, hover effects, and slide panels.',
                            'title': 'CSS Keyframe Animations'}],
        'filename': 'ui-developer-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2z"/></svg>',
        'name': 'UI Developer Certification',
        'title': 'UI Developer Course | Master HTML5, CSS3 & JavaScript'},
    {   'badge': 'Web Developer',
        'cat': 'dev',
        'desc': 'Master React functional components, hooks (useState, useEffect), Redux Toolkit state, virtual DOM, '
                'route pages, and API integrations.',
        'faqs': [   {   'a': 'Yes, we recommend understanding basic JavaScript operations before starting React. We '
                             'cover a JavaScript refresher first.',
                        'q': 'Do I need to learn JavaScript first?'}],
        'features': [   {   'desc': 'Build modular web UI views using React functional components.',
                            'title': 'Functional Components'},
                        {   'desc': 'Manage states, side-effects, and context values with built-in hooks.',
                            'title': 'React Hooks System'},
                        {   'desc': 'Configure centralized, stateful data stores across complex components.',
                            'title': 'Redux Toolkit State'},
                        {   'desc': 'Build Single Page Applications (SPA) with fast, client-side routing layouts.',
                            'title': 'React Router DOM'},
                        {   'desc': 'Fetch, post, and display database records inside React templates.',
                            'title': 'REST API Integrations'},
                        {   'desc': 'Understand component render lifecycles and optimize performance.',
                            'title': 'Virtual DOM Performance'}],
        'filename': 'react-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 '
                '10-10-4.48-10-10-10z"/></svg>',
        'name': 'React JS Library',
        'title': 'React JS Library Course | Master React Hooks & Redux'},
    {   'badge': 'Web Developer',
        'cat': 'dev',
        'desc': 'Master Node.js asynchronous runtime operations, Express web framework APIs, MongoDB database '
                'operations, and deployment parameters.',
        'faqs': [   {   'a': 'We use MongoDB, the most popular NoSQL database for Node.js developer workflows, along '
                             'with Mongoose.',
                        'q': 'What database will we use?'}],
        'features': [   {   'desc': "Master Node's non-blocking I/O operations and asynchronous execution models.",
                            'title': 'Event Loop Architecture'},
                        {   'desc': 'Build fast, modular server backends using Express routers and middlewares.',
                            'title': 'Express Framework APIs'},
                        {   'desc': 'Store data records, design schema schemas using Mongoose ORM models.',
                            'title': 'MongoDB Database Integrations'},
                        {   'desc': 'Process massive files and video assets in memory streams safely.',
                            'title': 'Asynchronous Streams & Buffers'},
                        {   'desc': 'Secure APIs with cookie-sessions, token structures, and salted passwords.',
                            'title': 'Secure Authentications'},
                        {   'desc': 'Write unit tests and endpoint integration assertions for APIs.',
                            'title': 'API Testing (Jest & Supertest)'}],
        'filename': 'nodejs-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2z"/></svg>',
        'name': 'Node.js Developer',
        'title': 'Node.js Developer Course | Express & MongoDB APIs'},
    {   'badge': 'Cloud Specialist',
        'cat': 'cloud',
        'desc': 'Master AWS Cloud infrastructure, compute, networking, security, storage databases, and architecture '
                'designs from experts.',
        'faqs': [   {   'a': 'Yes! The course matches both AWS SysOps and Solutions Architect Associate exam '
                             'guidelines.',
                        'q': 'Does this cover the Solutions Architect exam?'}],
        'features': [   {   'desc': 'Configure virtual servers, configure scale thresholds, and load balancers.',
                            'title': 'AWS Compute EC2 & Auto-scale'},
                        {   'desc': 'Design secure subnets, configure route tables, gateways, and security groups.',
                            'title': 'VPC Network Configurations'},
                        {   'desc': 'Define user groups, policy rules, roles, and cross-account access parameters.',
                            'title': 'IAM Security Vaults'},
                        {   'desc': 'Configure object buckets, lifecycle rules, database volumes, and replication.',
                            'title': 'Storage Solutions (S3 & EFS)'},
                        {   'desc': 'Deploy high-availability MySQL/PostgreSQL instances with read-replicas.',
                            'title': 'AWS RDS Databases'},
                        {   'desc': 'Build dashboards, log configurations, and email alert actions.',
                            'title': 'CloudWatch & Alert Monitors'}],
        'filename': 'aws-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 '
                '8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>',
        'name': 'AWS Cloud Practitioner & SysOps',
        'title': 'AWS Cloud Practitioner & SysOps Course | Master AWS Infrastructure'},
    {   'badge': 'Cloud Specialist',
        'cat': 'cloud',
        'desc': 'Master Microsoft Azure administration, virtual network designs, virtual machines, resource managers, '
                'active directories, and backups.',
        'faqs': [   {   'a': 'Yes, our training is fully aligned with the official AZ-104 Azure Administrator '
                             'Associate exam.',
                        'q': 'Is this AZ-104 aligned?'}],
        'features': [   {   'desc': 'Deploy virtual instances, auto-scale sizes, and load balancing rules.',
                            'title': 'Azure VMs & Scale Sets'},
                        {   'desc': 'Design subnet layouts, configure peering, firewalls, and route routes.',
                            'title': 'Azure VNet Networks'},
                        {   'desc': 'Manage user groups, credentials, access rules, and single-sign-on.',
                            'title': 'Microsoft Entra ID (Active Directory)'},
                        {   'desc': 'Store massive files, configure redundancy, and access keys.',
                            'title': 'Storage Accounts & Blob File Shares'},
                        {   'desc': 'Automate resource provisioning using declarative JSON template scripts.',
                            'title': 'ARM Template Deployments'},
                        {   'desc': 'Analyze system performance, log metrics, and check costs.',
                            'title': 'Azure Monitor & Logs'}],
        'filename': 'azure-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 '
                '8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>',
        'name': 'Microsoft Azure Administrator',
        'title': 'Microsoft Azure Administrator Course | Master AZ-104'},
    {   'badge': 'Cloud Specialist',
        'cat': 'cloud',
        'desc': 'Master Google Cloud services, compute engines, VPC networking networks, Cloud Storage buckets, '
                'BigQuery analytics, and IAM safety rules.',
        'faqs': [   {   'a': "We guide you in setting up GCP's official free tier account which includes $300 in free "
                             'usage credits.',
                        'q': 'Do you provide GCP credits?'}],
        'features': [   {   'desc': 'Provision Linux/Windows virtual machines, scale parameters, and disks.',
                            'title': 'Compute Engine Instances'},
                        {   'desc': 'Build virtual network layers, subnets, routers, and firewall setups.',
                            'title': 'GCP VPC Networking'},
                        {   'desc': 'Configure storage classes, lifecycles, and object permissions safely.',
                            'title': 'Cloud Storage Buckets'},
                        {   'desc': 'Set up organization permissions, service accounts, and key files.',
                            'title': 'IAM Security Policies'},
                        {   'desc': 'Query huge datasets serverless using standard SQL dashboards.',
                            'title': 'BigQuery Analytics'},
                        {   'desc': "Deploy containerized applications on Google's managed Kubernetes engine.",
                            'title': 'GKE Kubernetes Engine'}],
        'filename': 'gcp-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2z"/></svg>',
        'name': 'Google Cloud Associate Architect',
        'title': 'Google Cloud Associate Architect Course | Master GCP Cloud'},
    {   'badge': 'Cloud Specialist',
        'cat': 'cloud',
        'desc': 'Master DevOps engineering, Docker containers, Kubernetes orchestrations, Jenkins CI/CD pipelines, '
                'Git, Ansible configs, and Terraform IaC.',
        'faqs': [   {   'a': 'DevOps engineering positions are extremely lucrative due to automated pipeline scaling '
                             'dependencies.',
                        'q': 'What is the average salary of a DevOps engineer?'}],
        'features': [   {   'desc': 'Build container images, run registries, and manage system networks.',
                            'title': 'Docker Containers'},
                        {   'desc': 'Deploy deployments, services, pods, ingress routers, and configmaps.',
                            'title': 'Kubernetes Clusters'},
                        {   'desc': 'Write declarative Groovy scripts to automate build and deploy pipelines.',
                            'title': 'Jenkins CI/CD Pipelines'},
                        {   'desc': 'Write declarative config files to deploy cloud networks automatically.',
                            'title': 'Terraform (IaC)'},
                        {   'desc': 'Automate software installations and patches across multiple target servers.',
                            'title': 'Ansible Configurations'},
                        {   'desc': 'Master branching, pull requests, merges, and release workflows.',
                            'title': 'Git Version Control'}],
        'filename': 'devops-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 '
                '2-2V6c0-1.1-.9-2-2-2zm-5 14H4v-4h11v4zm0-5H4V9h11v4z"/></svg>',
        'name': 'DevOps Engineer Master',
        'title': 'DevOps Engineer Master Course | Docker, Kubernetes & Jenkins'},
    {   'badge': 'Testing Specialist',
        'cat': 'security',
        'desc': 'Master Selenium WebDriver, TestNG, page object models (POM), Maven build tools, and automated web '
                'testing workflows using Java or Python.',
        'features': [   {   'desc': 'Locate elements using XPath, CSS selectors, IDs, and execute browser actions.',
                            'title': 'Selenium WebDriver'},
                        {   'desc': 'Write test assertions, configure suites, group tests, and generate reports.',
                            'title': 'TestNG / JUnit Frameworks'},
                        {   'desc': 'Design scalable, maintainable test architectures separating page objects and '
                                    'tests.',
                            'title': 'Page Object Model (POM)'},
                        {   'desc': 'Parameterize test scripts using Apache POI to read Excel sheets or properties.',
                            'title': 'Data-Driven Testing'},
                        {   'desc': 'Execute test suites automatically via Jenkins pipelines and Maven goals.',
                            'title': 'CI/CD & Jenkins Integration'},
                        {   'desc': 'Run automated scripts across multiple browsers and OS nodes concurrently.',
                            'title': 'Grid & Parallel Executions'}],
        'filename': 'selenium-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'Selenium Automation Testing',
        'title': 'Selenium Automation Testing Training | Master WebDriver & Frameworks'},
    {   'badge': 'Testing Specialist',
        'cat': 'security',
        'desc': 'Master Playwright automation with JavaScript/TypeScript. Learn modern browser automation, '
                'auto-waiting, trace viewers, and multi-browser execution.',
        'features': [   {   'desc': 'Learn page interactions, auto-waiting, locators, and dynamic assertion logic.',
                            'title': 'Playwright Core Concepts'},
                        {   'desc': 'Write modern, async-await testing scripts inside Node environments.',
                            'title': 'JavaScript / TypeScript Setup'},
                        {   'desc': "Use Playwright's visual debugger and trace viewer to isolate failed tests.",
                            'title': 'Playwright Inspector & Trace'},
                        {   'desc': 'Mock API network responses, monitor traffic, and validate API integration '
                                    'endpoints.',
                            'title': 'API & Network Interception'},
                        {   'desc': 'Run tests concurrently across Chromium, Firefox, and WebKit rendering engines.',
                            'title': 'Parallel Executions'},
                        {   'desc': 'Configure Playwright suites to execute automatically inside GitHub Actions '
                                    'pipelines.',
                            'title': 'CI Integration & Actions'}],
        'filename': 'playwright-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'Playwright Test Automation',
        'title': 'Playwright Test Automation Training | Modern End-to-End Testing'},
    {   'badge': 'Testing Specialist',
        'cat': 'security',
        'desc': 'Master manual API testing with Postman and automated API validations with Java RestAssured. Validate '
                'JSON, schemas, and authentication headers.',
        'features': [   {   'desc': 'Send GET, POST, PUT, DELETE requests with headers, payloads, and parameters in '
                                    'Postman.',
                            'title': 'Manual API Verification'},
                        {   'desc': 'Write JavaScript assertions in Postman to validate status codes and response '
                                    'bodies.',
                            'title': 'Postman Test Scripting'},
                        {   'desc': 'Configure Maven dependencies, write BDD-style given-when-then automated test '
                                    'scripts.',
                            'title': 'RestAssured Setup (Java)'},
                        {   'desc': 'De-serialize complex response payloads into custom Java models for verification.',
                            'title': 'JSON / XML Body Parsing'},
                        {   'desc': 'Handle bearer login tokens, session keys, and API key authentication headers.',
                            'title': 'Token-based Auth (JWT/OAuth)'},
                        {   'desc': 'Orchestrate Postman collections from CLI for automated CI pipeline checks.',
                            'title': 'Newman CLI Automation'}],
        'filename': 'api-testing-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'API Testing & Automation',
        'title': 'API Testing & Automation Training | Postman & RestAssured'},
    {   'badge': 'Testing Specialist',
        'cat': 'security',
        'desc': 'Master performance testing, load testing, and stress testing workflows using Apache JMeter. Monitor '
                'servers, analyze bottlenecks, and generate reports.',
        'features': [   {   'desc': 'Understand load, stress, spike, endurance testing, and transaction metrics.',
                            'title': 'Performance Test Strategies'},
                        {   'desc': 'Configure virtual users, ramp-up schedules, loop counts, and duration timers.',
                            'title': 'JMeter Thread Groups'},
                        {   'desc': 'Parse response parameters using JSON Path and Regular Expression Extractors.',
                            'title': 'Assertions & Extractors'},
                        {   'desc': 'Inject test parameters using CSV Data Set Configs to simulate unique users.',
                            'title': 'Data Parameterization'},
                        {   'desc': 'Configure master-slave JMeter nodes to generate heavy user concurrency.',
                            'title': 'Distributed Load Generation'},
                        {   'desc': 'Analyze HTML reports, throughput, latency profiles, and identify bottlenecks.',
                            'title': 'Dashboard Reporting'}],
        'filename': 'jmeter-training.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'JMeter Performance Testing',
        'title': 'Apache JMeter Performance Testing Training | Master Load & Stress Tests'},
    {   'badge': 'Testing Specialist',
        'cat': 'security',
        'desc': 'Master software testing lifecycles, test planning, writing test cases, defect tracking in Jira, Agile '
                'Scrum QA process, and database basics.',
        'features': [   {   'desc': 'Understand waterfall and agile cycles, and the phases of testing lifecycles.',
                            'title': 'SDLC & STLC Processes'},
                        {   'desc': 'Write clear test cases with preconditions, test steps, expected and actual '
                                    'results.',
                            'title': 'Test Case Designing'},
                        {   'desc': 'Log defects in Jira with severity, priority, description, and steps to reproduce.',
                            'title': 'Defect Lifecycle & Tracking'},
                        {   'desc': 'Apply Equivalence Partitioning, Boundary Value Analysis, and Decision Tables.',
                            'title': 'Black Box Test Designs'},
                        {   'desc': 'Write basic SQL SELECT queries to verify backend tables during tests.',
                            'title': 'Database Verification (SQL)'},
                        {   'desc': 'Participate in sprint planning, stand-ups, retro reviews, and burndown charts.',
                            'title': 'Agile QA Practices'}],
        'filename': 'manual-testing.html',
        'icon': '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 '
                '2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
        'name': 'Manual QA & Software Testing',
        'title': 'Manual QA & Software Testing Course | Master QA Methodologies'}]

# Safe replacement string templates
template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>_PAGE_TITLE_ - KS Trainings</title>
<meta name="description" content="_PAGE_DESC_">
<link rel="canonical" href="https://kstrainings.com/_FILENAME_">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body { font-family: 'Inter', 'Segoe UI', Arial, sans-serif; color: #1a2456; background: #fff; line-height: 1.6; }
  a { text-decoration: none; color: inherit; }
  img { max-width: 100%; }

  .top-bar { background: #1a2456; color: #fff; padding: 8px 0; font-size: 0.82rem; }
  .top-bar-inner { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }
  .top-contact { display: flex; gap: 20px; align-items: center; flex-wrap: wrap; }
  .top-contact a { color: #ccc; display: flex; align-items: center; gap: 6px; transition: color .2s; }
  .top-contact a:hover { color: #f59e0b; }

  header { background: #fff; border-bottom: 1px solid #e5e7eb; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 8px rgba(0,0,0,.06); }
  .header-inner { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; height: 70px; }
  .logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
  .logo img { 
    height: 52px; width: 52px; 
    object-fit: contain; 
    border-radius: 50%; 
    border: 2px solid #002244; 
    box-shadow: 0 0 12px rgba(0, 34, 68, 0.2);
    background: #fff;
    padding: 2px;
  }
  .logo-name { 
    font-size: 1.45rem; 
    font-weight: 900; 
    color: #002244; /* Nexa Blue */
    text-transform: uppercase;
    letter-spacing: 0.5px;
    line-height: 1.1;
  }
  .logo-sub { 
    font-size: 0.68rem; 
    color: #2563eb; /* Complementary accent blue */
    font-weight: 700; 
    letter-spacing: .1em; 
    text-transform: uppercase; 
    margin-top: 2px;
  }
  nav { display: flex; align-items: center; gap: 4px; }
  nav a { color: #374151; font-weight: 600; font-size: 0.85rem; padding: 8px 12px; border-radius: 6px; transition: .2s; text-transform: uppercase; letter-spacing: .02em; }
  nav a:hover, nav a.active { color: #1a2456; background: #f3f4f6; }
  .btn-demo { background: #1a2456 !important; color: #fff !important; padding: 10px 20px !important; border-radius: 6px; font-weight: 700 !important; }
  .btn-demo:hover { background: #2563eb !important; }
  .menu-toggle { display: none; background: none; border: 1.5px solid #d1d5db; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 1.1rem; color: #374151; }

  /* HERO */
  .hero { background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #7c3aed 100%); padding: 80px 0 60px; position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; inset: 0; background: url('https://images.unsplash.com/photo-1573164713988-8665fc963095?auto=format&fit=crop&w=1200&q=60') center/cover; opacity: .07; }
  .hero-inner { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; gap: 50px; position: relative; }
  .hero-text { flex: 1; }
  .hero-badge { display: inline-block; background: rgba(124,58,237,.2); border: 1px solid rgba(124,58,237,.5); color: #a78bfa; font-size: 0.78rem; font-weight: 700; padding: 5px 14px; border-radius: 20px; margin-bottom: 18px; text-transform: uppercase; letter-spacing: .08em; }
  .hero-text h1 { font-size: clamp(1.8rem, 3.5vw, 2.8rem); font-weight: 800; color: #fff; line-height: 1.15; margin-bottom: 16px; }
  .hero-text h1 span { color: #f59e0b; }
  .hero-text p { color: rgba(255,255,255,.8); font-size: 1.05rem; margin-bottom: 30px; max-width: 540px; line-height: 1.7; }
  .hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }
  .btn-primary { background: #f59e0b; color: #1a2456; font-weight: 700; padding: 13px 28px; border-radius: 6px; font-size: 0.9rem; transition: .2s; border: 2px solid #f59e0b; display: inline-block; }
  .btn-primary:hover { background: transparent; color: #f59e0b; }
  .btn-outline { background: transparent; color: #fff; font-weight: 700; padding: 13px 28px; border-radius: 6px; font-size: 0.9rem; border: 2px solid rgba(255,255,255,.4); display: inline-block; transition: .2s; }
  .btn-outline:hover { border-color: #fff; background: rgba(255,255,255,.1); }
  .hero-img-circle { width: 180px; height: 180px; border-radius: 50%; background: rgba(255, 255, 255, 0.1); border: 2px solid rgba(255,255,255,0.25); display: flex; align-items: center; justify-content: center; backdrop-filter: blur(8px); flex-shrink: 0; }
  .hero-img-circle svg { width: 90px; height: 90px; fill: #f59e0b; }
  
  .stats-band { background: rgba(255,255,255,.06); backdrop-filter: blur(8px); border-top: 1px solid rgba(255,255,255,.1); margin-top: 50px; }
  .stats-inner { max-width: 1200px; margin: 0 auto; padding: 24px 20px; display: grid; grid-template-columns: repeat(4, 1fr); text-align: center; gap: 20px; }
  .stat-item .num { font-size: 2rem; font-weight: 800; color: #f59e0b; }
  .stat-item .lbl { font-size: 0.82rem; color: rgba(255,255,255,.7); margin-top: 2px; }

  .section { padding: 70px 0; }
  .section-alt { background: #f8faff; }
  .section-inner { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
  .section-title { text-align: center; margin-bottom: 48px; }
  .section-title h2 { font-size: clamp(1.5rem, 3vw, 2.1rem); font-weight: 800; color: #1a2456; margin-bottom: 10px; }
  .section-title p { color: #6b7280; font-size: 1rem; max-width: 620px; margin: 0 auto; }
  .divider { width: 60px; height: 4px; background: linear-gradient(90deg, #7c3aed, #f59e0b); border-radius: 2px; margin: 16px auto 0; }

  /* SERVICES GRID */
  .services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
  .svc-card { background: #fff; border: 1px solid #e5e7eb; border-radius: 14px; padding: 32px 24px; transition: .25s; }
  .svc-card:hover { transform: translateY(-6px); box-shadow: 0 16px 40px rgba(124,58,237,.12); border-color: #7c3aed; }
  .svc-icon { width: 56px; height: 56px; background: linear-gradient(135deg, #f3f0ff, #ede9fe); border-radius: 14px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; }
  .svc-icon svg { width: 28px; height: 28px; fill: #7c3aed; }
  .svc-card h3 { font-size: 1.05rem; font-weight: 700; color: #1a2456; margin-bottom: 10px; }
  .svc-card p { color: #6b7280; font-size: 0.9rem; line-height: 1.65; }

  /* WHY US */
  .why-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
  .why-card { text-align: center; padding: 32px 20px; background: #fff; border-radius: 14px; border: 1px solid #e5e7eb; }
  .why-icon { width: 64px; height: 64px; background: linear-gradient(135deg, #7c3aed, #2563eb); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; }
  .why-icon svg { width: 30px; height: 30px; fill: #fff; }
  .why-card h4 { font-size: 1rem; font-weight: 700; color: #1a2456; margin-bottom: 8px; }
  .why-card p { color: #6b7280; font-size: 0.88rem; }

  /* PROCESS */
  .process-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; position: relative; }
  .process-grid::before { content: ''; position: absolute; top: 36px; left: 12.5%; right: 12.5%; height: 2px; background: #e5e7eb; z-index: 0; }
  .step { text-align: center; padding: 0 16px; position: relative; z-index: 1; }
  .step-num { width: 72px; height: 72px; background: linear-gradient(135deg, #7c3aed, #2563eb); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 18px; font-size: 1.5rem; font-weight: 800; color: #fff; border: 4px solid #fff; box-shadow: 0 4px 16px rgba(124,58,237,.25); }
  .step h4 { font-size: 1rem; font-weight: 700; color: #1a2456; margin-bottom: 8px; }
  .step p { color: #6b7280; font-size: 0.88rem; }

  /* FAQ */
  .faq-list { max-width: 820px; margin: 0 auto; }
  .faq-item { border: 1px solid #e5e7eb; border-radius: 10px; margin-bottom: 12px; overflow: hidden; }
  .faq-q { width: 100%; background: #fff; border: none; padding: 18px 24px; text-align: left; font-family: inherit; font-size: 1rem; font-weight: 600; color: #1a2456; cursor: pointer; display: flex; align-items: center; justify-content: space-between; transition: .2s; }
  .faq-q:hover { background: #faf5ff; }
  .faq-q .arrow { font-size: 1.2rem; transition: transform .3s; color: #7c3aed; }
  .faq-item.open .faq-q { background: #f3f0ff; }
  .faq-item.open .arrow { transform: rotate(180deg); }
  .faq-a { display: none; padding: 0 24px 18px; color: #374151; font-size: 0.93rem; line-height: 1.75; background: #faf5ff; }
  .faq-item.open .faq-a { display: block; }

  /* FORM */
  .form-section { background: linear-gradient(135deg, #0f172a, #1e1b4b, #312e81); padding: 70px 0; }
  .form-wrap { max-width: 720px; margin: 0 auto; padding: 0 20px; }
  .form-card { background: #fff; border-radius: 20px; padding: 44px 40px; box-shadow: 0 24px 60px rgba(0,0,0,.25); }
  .form-card h2 { font-size: 1.7rem; font-weight: 800; color: #1a2456; margin-bottom: 6px; }
  .form-card p { color: #6b7280; margin-bottom: 28px; }
  .form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .form-group { display: flex; flex-direction: column; gap: 6px; }
  .form-group.full { grid-column: 1 / -1; }
  .form-group label { font-size: 0.85rem; font-weight: 600; color: #374151; }
  .form-control { border: 1.5px solid #d1d5db; border-radius: 8px; padding: 11px 14px; font-size: 0.9rem; font-family: inherit; color: #1a2456; transition: .2s; background: #fff; width: 100%; }
  .form-control:focus { outline: none; border-color: #7c3aed; box-shadow: 0 0 0 3px rgba(124,58,237,.1); }
  .btn-submit { background: linear-gradient(135deg, #7c3aed, #2563eb); color: #fff; border: none; border-radius: 8px; padding: 14px 32px; font-size: 1rem; font-weight: 700; cursor: pointer; width: 100%; margin-top: 8px; font-family: inherit; transition: .2s; }
  .btn-submit:hover { opacity: .9; transform: translateY(-1px); }

  /* FOOTER */
  footer { background: #0f172a; color: #fff; padding: 60px 0 0; }
  .footer-inner { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
  .footer-grid { display: grid; grid-template-columns: 1.8fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 40px; }
  .footer-brand p { color: rgba(255,255,255,.6); font-size: .88rem; margin-top: 12px; line-height: 1.7; }
  .footer-logo-name { font-size: 1.4rem; font-weight: 800; color: #fff; }
  .footer-col h5 { font-size: .88rem; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: #a78bfa; margin-bottom: 16px; }
  .footer-col a { display: block; color: rgba(255,255,255,.65); font-size: .88rem; margin-bottom: 10px; transition: .2s; }
  .footer-col a:hover { color: #fff; }
  .footer-bottom { border-top: 1px solid rgba(255,255,255,.1); padding: 20px 0; text-align: center; color: rgba(255,255,255,.5); font-size: .82rem; }

  /* WHATSAPP FLOAT */
  .whatsapp-float { position: fixed; right: 22px; bottom: 22px; z-index: 999; background: #25d366; border-radius: 50%; width: 58px; height: 58px; display: flex; align-items: center; justify-content: center; box-shadow: 0 6px 20px rgba(37,211,102,.4); transition: .2s; }
  .whatsapp-float:hover { transform: scale(1.1); }

  

  /* Unified Floating Widgets Styles (Glowing WhatsApp + Standardized Chatbot) */
  .whatsapp-float {
    position: fixed;
    right: 22px;
    bottom: 22px;
    z-index: 999;
    background: #25d366;
    border-radius: 50%;
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 0 0 rgba(37,211,102, 0.6);
    animation: wa-glow-animation 2s infinite;
    transition: transform .2s;
  }
  .whatsapp-float:hover {
    transform: scale(1.1);
  }
  .whatsapp-float svg {
    width: 32px;
    height: 32px;
    fill: #fff;
  }
  @keyframes wa-glow-animation {
    0% {
      box-shadow: 0 0 0 0 rgba(37,211,102, 0.7);
    }
    70% {
      box-shadow: 0 0 0 20px rgba(37,211,102, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(37,211,102, 0);
    }
  }

  .chat-fab {
    position: fixed;
    right: 22px;
    bottom: 90px;
    z-index: 999;
    background: linear-gradient(135deg, #7c3aed, #2563eb);
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 58px;
    height: 58px;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 16px rgba(124,58,237,.3);
    cursor: pointer;
    transition: transform .2s;
  }
  .chat-fab:hover {
    transform: scale(1.1);
  }
  .chat-fab .chat-dot {
    position: absolute;
    top: 12px;
    right: 12px;
    width: 10px;
    height: 10px;
    background: #22c55e;
    border-radius: 50%;
    border: 2px solid #fff;
  }

  .chat-panel {
    position: fixed;
    right: 22px;
    bottom: 164px;
    width: 350px;
    height: 480px;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0,0,0,.15);
    z-index: 999;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    opacity: 0;
    pointer-events: none;
    transform: translateY(20px);
    transition: opacity 0.25s ease, transform 0.25s ease;
  }
  .chat-panel.active {
    opacity: 1;
    pointer-events: auto;
    transform: translateY(0);
  }

  .chat-head {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    padding: 16px;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .chat-head-info {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .chat-head-av {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #fff;
    color: #7c3aed;
    display: grid;
    place-items: center;
    font-weight: 800;
    font-size: 0.85rem;
  }
  .chat-head-text h4 {
    font-size: 0.9rem;
    font-weight: 700;
    margin: 0;
  }
  .chat-head-text span {
    font-size: 0.72rem;
    opacity: 0.85;
    display: block;
  }
  .chat-close {
    background: none;
    border: none;
    color: #fff;
    cursor: pointer;
    font-size: 1.4rem;
    opacity: .8;
    transition: opacity .2s;
  }
  .chat-close:hover {
    opacity: 1;
  }

  .chat-body {
    flex: 1;
    padding: 16px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
    background: #f8fafc;
  }
  .msg-row {
    display: flex;
    width: 100%;
    margin-bottom: 4px;
  }
  .msg-row.bot {
    justify-content: flex-start;
  }
  .msg-row.user {
    justify-content: flex-end;
  }
  .msg-bubble {
    max-width: 85%;
    padding: 10px 14px;
    border-radius: 12px;
    font-size: 0.88rem;
    line-height: 1.45;
  }
  .msg-row.bot .msg-bubble {
    background: #fff;
    border: 1px solid #e2e8f0;
    border-bottom-left-radius: 4px;
    color: #1a2456;
  }
  .msg-row.user .msg-bubble {
    background: #7c3aed;
    color: #fff;
    border-bottom-right-radius: 4px;
  }

  .chat-quick {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    padding: 8px 12px;
    border-top: 1px solid #e2e8f0;
    background: #f8fafc;
  }
  .chat-quick button {
    font-size: 0.72rem;
    padding: 5px 10px;
    border-radius: 999px;
    border: 1px solid #cbd5e1;
    background: #fff;
    color: #475569;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
    font-weight: 500;
  }
  .chat-quick button:hover {
    border-color: #7c3aed;
    color: #7c3aed;
    background: #faf5ff;
  }

  .chat-foot {
    padding: 12px;
    background: #fff;
    border-top: 1px solid #e2e8f0;
    display: flex;
    gap: 8px;
  }
  .chat-input {
    flex: 1;
    border: 1px solid #cbd5e1;
    border-radius: 999px;
    padding: 8px 14px;
    outline: none;
    font-size: 0.88rem;
    font-family: inherit;
    transition: border-color .2s;
  }
  .chat-input:focus {
    border-color: #7c3aed;
  }
  .chat-send {
    background: #7c3aed;
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    cursor: pointer;
    display: grid;
    place-items: center;
    transition: background .2s;
  }
  .chat-send:hover {
    background: #2563eb;
  }
</style>
</head>

<body>

<!-- TOP BAR -->
<div class="top-bar">
  <div class="top-bar-inner">
    <div class="top-contact">
      <a href="mailto:info@kstrainings.com">&#9993; info@kstrainings.com</a>
      <a href="tel:+918675539226">&#128222; +91-8675539226</a>
    </div>
    <span style="color:rgba(255,255,255,.5);font-size:.8rem;">_PAGE_NAME_ Training &amp; Certification Program</span>
  </div>
</div>

<!-- HEADER -->
<header>
  <div class="header-inner">
    <div class="logo">
      <img src="ks-logo.jpg" alt="KS Trainings Logo" onerror="this.style.display='none'">
      <div>
        <div class="logo-name">KS Trainings</div>
        <div class="logo-sub">An Online Training Portal</div>
      </div>
    </div>
    <nav id="mainNav">
      <a href="index.html">Home</a>
      <a href="courses.html">Courses</a>
      <a href="video-editing.html">Video Editing</a>
      <a href="social-media-management.html">Social Media</a>
      <a href="on-job-support.html">On-Job Support</a>
      <a href="#demo-form" class="btn-demo">Get Free Quote</a>
    </nav>
    <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu">&#9776;</button>
  </div>
</header>

<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <div class="hero-text">
      <div class="hero-badge">_PAGE_BADGE_ Training</div>
      <h1>Master <span>_PAGE_NAME_</span> with Live Expert Mentors</h1>
      <p>_PAGE_DESC_</p>
      <div class="hero-btns">
        <a href="#demo-form" class="btn-primary">Book A Free Demo</a>
        <a href="#services" class="btn-outline">Explore Syllabus</a>
      </div>
    </div>
    <div class="hero-img-circle">
      _PAGE_ICON_
    </div>
  </div>
  <div class="stats-band">
    <div class="stats-inner">
      <div class="stat-item"><div class="num">100%</div><div class="lbl">Job-Oriented Training</div></div>
      <div class="stat-item"><div class="num">10+ Yrs</div><div class="lbl">MNC Expert Trainers</div></div>
      <div class="stat-item"><div class="num">15+</div><div class="lbl">Hands-on Lab Projects</div></div>
      <div class="stat-item"><div class="num">24/7</div><div class="lbl">Post-Course Support</div></div>
    </div>
  </div>
</section>

<!-- SERVICES / COURSE MODULES -->
<section class="section" id="services">
  <div class="section-inner">
    <div class="section-title">
      <h2>Syllabus &amp; Training Modules</h2>
      <p>A comprehensive, real-world curriculum designed to take you from basics to expert level workflows.</p>
      <div class="divider"></div>
    </div>
    <div class="services-grid">
      _MODULES_HTML_
    </div>
  </div>
</section>

<!-- WHY CHOOSE US -->
<section class="section section-alt">
  <div class="section-inner">
    <div class="section-title">
      <h2>Why Train with KS Trainings?</h2>
      <p>We provide a reliable, highly interactive, and career-focused learning ecosystem.</p>
      <div class="divider"></div>
    </div>
    <div class="why-grid">
      <div class="why-card">
        <div class="why-icon"><svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 4l5 2.18V11c0 3.5-2.33 6.79-5 7.93-2.67-1.14-5-4.43-5-7.93V7.18L12 5z"/></svg></div>
        <h4>Active Industry Experts</h4>
        <p>Learn from consultants working in top tech companies who handle real challenges daily.</p>
      </div>
      <div class="why-card">
        <div class="why-icon"><svg viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67V7z"/></svg></div>
        <h4>Practical Hands-On Labs</h4>
        <p>We focus heavily on live labs, sandbox tasks, and real MNC projects instead of slide presentations.</p>
      </div>
      <div class="why-card">
        <div class="why-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg></div>
        <h4>100% Placement Support</h4>
        <p>Get complete resume reviews, profile branding, and mock interviews with active hiring partners.</p>
      </div>
      <div class="why-card">
        <div class="why-icon"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></div>
        <h4>Silent On-Job Support</h4>
        <p>Get 1-on-1 backend technical support even after you land a job, helping you complete office tasks easily.</p>
      </div>
    </div>
  </div>
</section>

<!-- PROCESS -->
<section class="section">
  <div class="section-inner">
    <div class="section-title">
      <h2>Training to Placement Workflow</h2>
      <p>A simple, step-by-step career path designed to secure your target tech role quickly.</p>
      <div class="divider"></div>
    </div>
    <div class="process-grid">
      <div class="step">
        <div class="step-num">1</div>
        <h4>Free Demo Session</h4>
        <p>Book a free 30-minute alignment session to review your goals and meet your trainer.</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <h4>Live Project Learning</h4>
        <p>Attend interactive live sessions and complete real-time labs on a staging sandbox.</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <h4>Mock Preparation</h4>
        <p>Fine-tune your resume layout and prepare with technical mock interviews.</p>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <h4>Interviews &amp; Support</h4>
        <p>Attend client interviews with placement support and secure your IT career.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section section-alt" id="faq">
  <div class="section-inner">
    <div class="section-title">
      <h2>Frequently Asked Questions</h2>
      <p>Everything you need to know about our _PAGE_NAME_ training program.</p>
      <div class="divider"></div>
    </div>
    <div class="faq-list">
      _FAQ_HTML_

      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">How are the classes scheduled? <span class="arrow">&#8964;</span></button>
        <div class="faq-a">We offer flexible timings with batches during weekdays and weekends. Classes are held live via Zoom/Teams with recorded backups provided.</div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT FORM -->
<section class="form-section" id="demo-form">
  <div class="form-wrap">
    <div class="form-card">
      <h2>Request a Free Demo Class</h2>
      <p>Fill out the details below and our team will get in touch within 2 hours to align your free live demo slot.</p>
      <form onsubmit="event.preventDefault(); submitForm(this);">
        <input type="text" name="website" style="display:none;" tabindex="-1" autocomplete="off">
        <div class="form-grid">
          <div class="form-group">
            <label for="is_name">Full Name *</label>
            <input class="form-control" id="is_name" type="text" name="name" placeholder="Your full name" required>
          </div>
          <div class="form-group">
            <label for="is_email">Email Address *</label>
            <input class="form-control" id="is_email" type="email" name="email" placeholder="you@example.com" required>
          </div>
          <div class="form-group">
            <label for="is_phone">Phone / WhatsApp *</label>
            <input class="form-control" id="is_phone" type="tel" name="phone" placeholder="Mobile / WhatsApp Number *" required>
          </div>
          <div class="form-group">
            <label for="is_course">Technology / Course *</label>
            <input class="form-control" id="is_course" type="text" name="course" value="_PAGE_NAME_" required readonly>
          </div>
          <div class="form-group full">
            <label for="is_support">What do you need support with? *</label>
            <select class="form-control" id="is_support" name="support_type" required>
              <option value="Training &amp; Certification" selected>Training &amp; Certification</option>
              <option value="On-Job Support">On-Job Support</option>
              <option value="Proxy Interview Support">Proxy Interview Support</option>
            </select>
          </div>
          <div class="form-group full">
            <label for="is_desc">Describe your goals / timeline *</label>
            <textarea class="form-control" id="is_desc" name="description" rows="3" placeholder="Let us know your current background and when you want to start..." required></textarea>
          </div>
          <div class="form-group full">
            <label for="is_captcha">Anti-Spam Check: What is 3 + 4? *</label>
            <input class="form-control" id="is_captcha" type="text" name="captcha" placeholder="Enter the answer" required>
          </div>
        </div>
        <button type="submit" id="ksSubmitBtn" class="btn-submit">Reserve My Free Demo Seat &rarr;</button>
        <div id="ksFormMsg" style="display:none;margin-top:14px;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;"></div>
      </form>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="footer-logo-name">KS Trainings</div>
        <p>IT training, video editing and social media management services. Trusted by 50,000+ professionals and 200+ brands worldwide. kstrainings.com</p>
      </div>
      <div class="footer-col">
        <h5>Quick Links</h5>
        <a href="index.html">Home</a>
        <a href="courses.html">IT Courses</a>
        <a href="video-editing.html">Video Editing</a>
        <a href="social-media-management.html">Social Media</a>
        <a href="on-job-support.html">On-Job Support</a>
        <a href="proxy-job-support.html">Proxy Support</a>
        <a href="proxy-interview-support.html">Interview Support</a>
      </div>
      <div class="footer-col">
        <h5>Our Services</h5>
        <a href="proxy-job-support.html">Daily Task Support</a>
        <a href="proxy-job-support.html">Bug Debugging</a>
        <a href="proxy-job-support.html">Code Optimization</a>
        <a href="proxy-interview-support.html">Interview Preparation</a>
      </div>
      <div class="footer-col">
        <h5>Contact Us</h5>
        <a href="tel:+918675539226">+91-8675539226</a>
        <a href="mailto:info@kstrainings.com">info@kstrainings.com</a>
        <a href="https://wa.me/918675539226" target="_blank">WhatsApp Us</a>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; 2025 KS Trainings. All rights reserved. | kstrainings.com | _PAGE_NAME_ Training &amp; Certification Program
    </div>
  </div>
</footer>


<!-- WHATSAPP FLOAT -->
<a href="https://wa.me/918675539226" target="_blank" class="whatsapp-float" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 32 32"><path d="M16 2a13 13 0 0 0-11 20l-2 7 7-2a13 13 0 1 0 6-25zm0 24c-2 0-4-1-6-2l-1-1-4 1 1-4-1-1a11 11 0 1 1 11 7zm6-9c0-.2-.1-.4-.5-.6l-3-1c-.2 0-.4 0-.5.1l-1 2c-.2.1-.4.1-.7 0a8 8 0 0 1-4-4c-.1-.3 0-.5.2-.7l1-1c.1-.2.2-.4.1-.6l-1-3c-.1-.3-.3-.4-.5-.4h-.5c-.3 0-.7.1-1 .5a4 4 0 0 0-1 3c0 2 1 4 2 5 2 3 5 5 8 6 1 0 3 0 4-1 .4-.4.6-1 .6-1 0-.2-.1-.4-.5-.6z"/></svg>
</a>

<!-- CHATBOT -->
<button class="chat-fab" id="chatFab" aria-label="Open chat assistant">
  <svg viewBox="0 0 24 24" width="26" height="26" fill="#fff"><path d="M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
  <span class="chat-dot"></span>
</button>
<div class="chat-panel" id="chatPanel" role="dialog" aria-label="KS Trainings Chat Assistant">
  <div class="chat-head">
    <div class="chat-head-info">
      <div class="chat-head-av">KS</div>
      <div class="chat-head-text">
        <h4>KS Trainings Assistant</h4>
        <span>Online - Replies instantly</span>
      </div>
    </div>
    <button class="chat-close" id="chatClose" aria-label="Close chat">&times;</button>
  </div>
  <div class="chat-body" id="chatBody"></div>
  <div class="chat-quick" id="chatQuick">
    _PAGE_QUICK_TABS_
  </div>
  <div class="chat-foot">
    <input type="text" class="chat-input" id="chatInput" placeholder="Type your message..." autocomplete="off">
    <button class="chat-send" id="chatSend" aria-label="Send message">➤</button>
  </div>
</div>

<script>
  // Mobile nav toggle
  (function() {
    var menuToggle = document.getElementById('menuToggle');
    var mainNav = document.getElementById('mainNav');
    if (menuToggle && mainNav) {
      menuToggle.onclick = function() {
        mainNav.classList.toggle('open');
      };
    }
  })();

  // Chatbot logic
  (function() {
    var chatFab = document.getElementById('chatFab');
    var chatPanel = document.getElementById('chatPanel');
    var chatClose = document.getElementById('chatClose');
    var chatInput = document.getElementById('chatInput');
    var chatBody = document.getElementById('chatBody');
    var chatSend = document.getElementById('chatSend');
    var chatQuick = document.getElementById('chatQuick');
    var chatGreeted = false;

    if (!chatFab || !chatPanel || !chatClose || !chatInput || !chatBody || !chatSend) return;

    function openChat() {
      chatPanel.classList.add('active');
      if (!chatGreeted) {
        chatGreeted = true;
        botSay("Hello! Welcome to KS Trainings. How can I help you with _PAGE_NAME_ today?");
      }
      chatInput.focus();
    }
    
    chatFab.onclick = function() {
      if (chatPanel.classList.contains('active')) {
        chatPanel.classList.remove('active');
      } else {
        openChat();
      }
    };
    
    chatClose.onclick = function() {
      chatPanel.classList.remove('active');
    };

    function addMsg(who, html) {
      var row = document.createElement('div');
      row.className = 'msg-row ' + who;
      row.innerHTML = '<div class="msg-bubble">' + html + '</div>';
      chatBody.appendChild(row);
      chatBody.scrollTop = chatBody.scrollHeight;
    }
    
    function botSay(html) {
      setTimeout(function() { addMsg('bot', html); }, 400);
    }

    function botReply(text) {
      var m = text.toLowerCase();
      if(/course|demo|trial|free/.test(m))
        return "You can book a free demo class for our _PAGE_NAME_ program. Fill the form on this page or message us directly on WhatsApp.";
      if(/contact|call|phone|email|reach|whatsapp/.test(m))
        return "Mobile/WhatsApp: +91-8675539226<br>Email: info@kstrainings.com. We are available 24/7!";
      if(/support|on.?job|proxy|interview/.test(m))
        return "We offer expert on-job and proxy support for _PAGE_NAME_. Fill the form on this page to get a quote within 2 hours.";
      if(/hi|hello|hey/.test(m))
        return "Hello! How can I help you with _PAGE_NAME_ training or support today?";
      return "Thank you for your message. For immediate support and free session bookings, please call/WhatsApp us at +91-8675539226.";
    }

    function sendChat(q){
      if(!q.trim()) return;
      addMsg('user', q.replace(/</g,'&lt;'));
      chatInput.value = '';
      botSay(botReply(q));
    }
    
    chatSend.onclick = function() { sendChat(chatInput.value); };
    chatInput.onkeypress = function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        sendChat(chatInput.value);
      }
    };
    
    if (chatQuick) {
      chatQuick.onclick = function(e) {
        var btn = e.target.closest('button');
        if (btn) {
          e.preventDefault();
          sendChat(btn.getAttribute('data-q') || btn.textContent);
        }
      };
    }
  })();
</script>

<!-- FORM SUBMISSION - Formspree + localStorage -->
<script>
  var KS_APPS_SCRIPT_URL = 'APPS_SCRIPT_WEB_APP_URL_PLACEHOLDER';
    function submitForm(form) {
      var msgEl = document.getElementById('ksFormMsg');
      var btn = document.getElementById('ksSubmitBtn');
      if (!msgEl || !btn) return;
      if (form.elements['website'] && form.elements['website'].value !== '') return;
      var c = form.elements['captcha'];
      if (!c || c.value.trim() !== '7') {
        msgEl.style.cssText = 'display:block;background:#fee2e2;color:#b91c1c;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
        msgEl.textContent = 'Anti-spam check failed. Answer is 7.'; return;
      }
      var name = (form.elements['name'] ? form.elements['name'].value.trim() : '');
      var email = (form.elements['email'] ? form.elements['email'].value.trim() : '');
      var phone = (form.elements['phone'] ? form.elements['phone'].value.trim() : '');
      var course = (form.elements['course'] ? form.elements['course'].value.trim() : '');
      var supportType = (form.elements['support_type'] ? form.elements['support_type'].value : '');
      var description = (form.elements['description'] ? form.elements['description'].value.trim() : '');
      var pageName = (form.getAttribute('data-page') || document.title || 'Course Page').split('|')[0].trim();
      btn.disabled = true;
      msgEl.style.cssText = 'display:block;background:#eff6ff;color:#1d4ed8;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Submitting...';
      try {
        var rec = {id:Date.now(),submitted_at:new Date().toLocaleString('en-IN'),page:pageName,name:name,email:email,phone:phone,course_service:course,support_type:supportType,description:description,status:'New'};
        var all = JSON.parse(localStorage.getItem('ks_submissions')||'[]'); all.unshift(rec); localStorage.setItem('ks_submissions',JSON.stringify(all));
      } catch(e) {}
          function showOK() {
      if(msgEl) msgEl.style.display = 'none';
      if(form) form.reset();
      if(btn) btn.disabled = false;
      if (typeof triggerParty === 'function') {
        triggerParty(name);
      }
    }
      if (KS_APPS_SCRIPT_URL && KS_APPS_SCRIPT_URL !== 'APPS_SCRIPT_WEB_APP_URL_PLACEHOLDER') {
        fetch(KS_APPS_SCRIPT_URL, {method:'POST',body:JSON.stringify({page_name:pageName,name:name,email:email,phone:phone,course_service:course,support_type:supportType,description:description}),headers:{'Content-Type':'text/plain'}})
        .then(function(r){return r.json();}).then(function(){showOK();}).catch(function(){showOK();});
      } else { showOK(); }
    }
    var msgEl = document.getElementById('ksFormMsg');
    var btn   = document.getElementById('ksSubmitBtn');
    if (!msgEl || !btn) return;

    if (form.elements['website'] && form.elements['website'].value !== '') return;

    var captchaEl = form.elements['captcha'];
    if (!captchaEl || captchaEl.value.trim() !== '7') {
      msgEl.style.display = 'block';
      msgEl.style.background = '#fee2e2';
      msgEl.style.color = '#b91c1c';
      msgEl.textContent = 'Anti-spam check failed. The answer is 7 (3 + 4 = 7).';
      return;
    }

    var name    = form.elements['name']         ? form.elements['name'].value.trim()         : '';
    var email   = form.elements['email']        ? form.elements['email'].value.trim()        : '';
    var phone   = form.elements['phone']        ? form.elements['phone'].value.trim()        : '';
    var course  = form.elements['course']       ? form.elements['course'].value.trim()       : '';
    var support = form.elements['support_type'] ? form.elements['support_type'].value        : '';
    var desc    = form.elements['description']  ? form.elements['description'].value.trim()  : '';

    btn.disabled = true;
    msgEl.style.display = 'block';
    msgEl.style.background = '#eff6ff';
    msgEl.style.color = '#1d4ed8';
    msgEl.textContent = 'Submitting your enquiry, please wait...';

    try {
      var rec = { id: Date.now(), submitted_at: new Date().toLocaleString('en-IN'), name: name, email: email, phone: phone, course: course, support_type: support, description: desc, page: '_PAGE_NAME_ Course', status: 'New' };
      var all = JSON.parse(localStorage.getItem('ks_submissions') || '[]');
      all.unshift(rec);
      localStorage.setItem('ks_submissions', JSON.stringify(all));
    } catch(e) {}

        function showOK() {
      if(msgEl) msgEl.style.display = 'none';
      if(form) form.reset();
      if(btn) btn.disabled = false;
      if (typeof triggerParty === 'function') {
        triggerParty(name);
      }
    }

    if (FORMSPREE_ID !== 'YOUR_FORM_ID') {
      var fd = new FormData(form);
      fd.append('_replyto', email);
      fd.append('Phone', phone);
      fd.append('Course', course);
      fetch('https://formspree.io/f/' + FORMSPREE_ID, {
        method: 'POST', body: fd,
        headers: { 'Accept': 'application/json' }
      }).then(function(r){ return r.json(); })
        .then(function(){ showOK(); })
        .catch(function(){ showOK(); });
    } else {
      showOK();
    }
  }
</script>

<!-- ================= CONFETTI & POPUP ================= -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<style>
  .ks-success-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: transparent;
    z-index: 99999;
    display: none;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.4s ease;
  }
  .ks-success-overlay.show {
    display: flex;
    opacity: 1;
  }
  .ks-success-modal {
    background: white;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    max-width: 450px;
    width: 90%;
    box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
    transform: scale(0.8) translateY(20px);
    transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  .ks-success-overlay.show .ks-success-modal {
    transform: scale(1) translateY(0);
  }
  .ks-success-modal .check-icon {
    width: 80px; height: 80px;
    background: #10b981;
    color: white;
    font-size: 40px;
    line-height: 80px;
    border-radius: 50%;
    margin: 0 auto 20px auto;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    animation: popIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    animation-delay: 0.2s;
    opacity: 0;
    transform: scale(0);
  }
  @keyframes popIn {
    to { opacity: 1; transform: scale(1); }
  }
  .ks-success-modal h3 {
    font-size: 28px;
    color: #1e293b;
    margin-bottom: 10px;
    font-weight: 800;
  }
  .ks-success-modal p {
    color: #64748b;
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 25px;
  }
  .ks-success-modal .name-highlight {
    color: #2563eb;
    font-weight: 700;
  }
  .ks-success-modal button {
    background: #2563eb;
    color: white;
    border: none;
    padding: 14px 32px;
    border-radius: 50px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
  }
  .ks-success-modal button:hover {
    background: #1d4ed8;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
  }
</style>

<div class="ks-success-overlay" id="ksSuccessOverlay">
  <div class="ks-success-modal">
    <div class="check-icon">✓</div>
    <h3>Awesome!</h3>
    <p>Thank you <span class="name-highlight" id="ksSuccessName"></span> for reaching out.<br>Our team will contact you very soon!</p>
    <button onclick="closeSuccessPopup()">Continue</button>
  </div>
</div>

<script>
  function closeSuccessPopup() {
    var overlay = document.getElementById('ksSuccessOverlay');
    if(overlay) {
      overlay.classList.remove('show');
      setTimeout(function() { overlay.style.display = 'none'; }, 400);
    }
  }
  function triggerParty(userName) {
    var overlay = document.getElementById('ksSuccessOverlay');
    if(!overlay) return;
    document.getElementById('ksSuccessName').textContent = userName || 'there';
    overlay.style.display = 'flex';
    setTimeout(function() { overlay.classList.add('show'); }, 10);

    // Auto-close after 7 seconds
    setTimeout(function() {
      closeSuccessPopup();
    }, 4000);

    // Confetti Animation
    var duration = 3 * 1000;
    var end = Date.now() + duration;
    (function frame() {
      confetti({
        particleCount: 5,
        angle: 60,
        spread: 55,
        origin: { x: 0 },
        colors: ['#2563eb', '#10b981', '#f59e0b', '#ef4444'],
        zIndex: 100000
      });
      confetti({
        particleCount: 5,
        angle: 120,
        spread: 55,
        origin: { x: 1 },
        colors: ['#2563eb', '#10b981', '#f59e0b', '#ef4444'],
        zIndex: 100000
      });
      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    }());
  }
</script>
<!-- ================= END CONFETTI & POPUP ================= -->

<!-- ================= FAQ & MOBILE MENU JS ================= -->
<script>
  (function() {
    // Mobile Menu
    var menuToggle = document.getElementById('menuToggle');
    var mainNav = document.getElementById('mainNav');
    if (menuToggle && mainNav) {
      menuToggle.addEventListener('click', function() {
        if (mainNav.style.display === 'flex' && mainNav.style.flexDirection === 'column') {
          mainNav.style.display = 'none';
        } else {
          mainNav.style.display = 'flex';
          mainNav.style.flexDirection = 'column';
          mainNav.style.position = 'absolute';
          mainNav.style.top = '78px';
          mainNav.style.left = '0';
          mainNav.style.right = '0';
          mainNav.style.background = '#fff';
          mainNav.style.boxShadow = '0 10px 15px -3px rgba(0,0,0,0.1)';
          mainNav.style.padding = '20px';
          mainNav.style.zIndex = '1000';
        }
      });
    }

    // FAQ Accordion
    var faqQs = document.querySelectorAll('.faq-q');
    faqQs.forEach(function(btn) {
      btn.addEventListener('click', function() {
        var ans = this.nextElementSibling;
        if (ans) {
          if (ans.style.display === 'block') {
            ans.style.display = 'none';
          } else {
            ans.style.display = 'block';
          }
        }
      });
    });
  })();
</script>
<!-- ================= END FAQ & MOBILE MENU JS ================= -->

</body>

</html>
"""

def get_topic_faqs(name, badge, features):
    # Generates 5 topic-specific questions and answers dynamically
    faqs = []
    
    # 1. Prerequisite / Who can attend
    faqs.append({
        "q": f"What are the prerequisites for the {name} training course?",
        "a": f"There are no strict prerequisites. This {name} training program starts with the absolute fundamentals of the technology, syntax, and workflows before progressing to advanced enterprise implementations."
    })
    
    # 2. Labs & Projects
    project_topics = ", ".join([f['title'] for f in features[:3]])
    faqs.append({
        "q": f"Will I get hands-on labs and real projects to practice in {name}?",
        "a": f"Yes, definitely. Our {name} course is 80% practical. You will work on real-world projects covering {project_topics}. You will build and deploy these under the guidance of active industry mentors."
    })
    
    # 3. Certification Preparation
    faqs.append({
        "q": f"Does this {name} training prepare me for professional certification?",
        "a": f"Yes, our curriculum is fully aligned with the official syllabus and certification guidelines. We provide practice tests, exam dumps, and mock validations to ensure you clear the certification exam on your first attempt."
    })
    
    # 4. Career opportunities & Roles
    faqs.append({
        "q": f"What are the career options and roles after learning {name}?",
        "a": f"Learning {name} opens up excellent roles such as {badge}, Technical Consultant, QA Engineer, or Developer in leading MNCs. The demand for certified professionals in this space is growing rapidly with premium pay scales."
    })
    
    # 5. Access and Batch Schedule
    faqs.append({
        "q": f"What if I miss a live batch session for {name}?",
        "a": f"All live sessions are recorded and uploaded to your student portal. You get lifetime access to the recordings, class notes, staging sandboxes, and lab files so you can learn at your own pace."
    })
    
    # 6. Proxy / On-Job Support Question (Configured custom as requested)
    faqs.append({
        "q": f"Do you provide proxy job support or on-job support for {name}?",
        "a": f"Yes, we provide professional on-job support and proxy task assistance for {name} differently. Our experts work with you 1-on-1 to guide you through your daily tasks, troubleshoot complex {name} queries/pipelines/code, and help you resolve bugs silently and confidentially, which serves as the ultimate on-job success support."
    })
    
    return faqs

# Generate all course pages
for course in courses_db:
    # Build Modules HTML
    modules_html = ""
    for index, item in enumerate(course["features"]):
        modules_html += f"""      <div class="svc-card">
        <div class="svc-icon"><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg></div>
        <h3>{item['title']}</h3>
        <p>{item['desc']}</p>
      </div>
"""

    # Build FAQs HTML dynamically (incorporating at least 5 topic-related + 1 proxy support FAQ)
    course_faqs = get_topic_faqs(course["name"], course["badge"], course["features"])
    faq_html = ""
    for item in course_faqs:
        faq_html += f"""      <div class="faq-item">
        <button class="faq-q" onclick="toggleFaq(this)">{item['q']} <span class="arrow">&#8964;</span></button>
        <div class="faq-a">{item['a']}</div>
      </div>
"""

    # Build dynamic suggestion buttons HTML
    quick_tabs_html = f"""    <button data-q="Can I get the syllabus for {course['name']}?">Syllabus</button>
    <button data-q="What are the fees for {course['name']}?">Course Fees</button>
    <button data-q="Do you offer on-job support for {course['name']}?">On-Job Support</button>
    <button data-q="I want a free live demo for {course['name']}">Free Demo</button>
    <button data-q="How do I contact the {course['name']} trainer?">Contact</button>"""

    # Bulletproof string replacement
    page_content = template
    page_content = page_content.replace("_PAGE_QUICK_TABS_", quick_tabs_html)
    page_content = page_content.replace("_PAGE_TITLE_", course["title"])
    page_content = page_content.replace("_PAGE_DESC_", course["desc"])
    page_content = page_content.replace("_FILENAME_", course["filename"])
    page_content = page_content.replace("_PAGE_NAME_", course["name"])
    page_content = page_content.replace("_PAGE_BADGE_", course["badge"])
    page_content = page_content.replace("_PAGE_ICON_", course["icon"])
    page_content = page_content.replace("_MODULES_HTML_", modules_html)
    page_content = page_content.replace("_FAQ_HTML_", faq_html)

    full_path = os.path.join(r"D:\Anti_gravity\kstrainings.com", course["filename"])
    print(f"Generating {full_path}...")
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(page_content)

print("Course generation script setup complete!")
