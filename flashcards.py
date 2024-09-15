import streamlit as st
import random

class Flashcard:
    def __init__(self, question, answer, options=None, reason=None):
        self.question = question
        self.answer = answer
        self.options = options
        self.reason = reason

class FlashcardApp:
    def __init__(self):
        self.data_science_cards = [
            Flashcard("What is a popular Python library for data manipulation?", "Pandas", 
                      ["NumPy", "Pandas", "Matplotlib", "Scikit-learn"], 
                      reason="Pandas is a powerful library used for data manipulation and analysis, particularly useful for data frames."),
            Flashcard("What is the purpose of NumPy in Python?", "Numerical computing and array operations",
                      ["Data visualization", "Web scraping", "Numerical computing and array operations", "Database management"],
                      reason="NumPy provides support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on them."),
            Flashcard("What does ML stand for in data science?", "Machine Learning",
                      ["Metadata Learning", "Machine Language", "Machine Learning", "Model Logic"],
                      reason="Machine Learning refers to systems that learn from data patterns to make predictions or decisions without being explicitly programmed."),
            Flashcard("What is the purpose of data normalization?", "To scale features to a similar range",
                      ["To remove outliers", "To scale features to a similar range", "To create new features", "To reduce dimensionality"],
                      reason="Normalization helps ensure that features contribute equally to the model by scaling them to a similar range, improving training performance."),
            Flashcard("What is a common algorithm for classification?", "Decision Trees",
                      ["K-means", "Principal Component Analysis", "Decision Trees", "Linear Regression"],
                      reason="Decision Trees are widely used in classification tasks, where data is split into subsets based on feature values.")
        ]
        self.cloud_computing_cards = [
            Flashcard("What are the main components of AWS Global Infrastructure?", 
                      "AWS Regions, AWS Availability Zones, AWS Data Centers, AWS Edge Locations / Points of Presence",
                      ["AWS Regions, AWS Zones, AWS Servers", "AWS Regions, AWS Availability Zones, AWS Data Centers, AWS Edge Locations / Points of Presence", "AWS Clouds, AWS Centers, AWS Nodes", "AWS Regions, AWS Clusters, AWS Hubs"],
                      reason="These components form the physical infrastructure of AWS, allowing for global redundancy and low-latency connections."),
            Flashcard("What is IAM in AWS?", "Identity and Access Management",
                      ["Internet Access Management", "Identity and Access Management", "Infrastructure and Application Management", "Integration and Authorization Module"],
                      reason="IAM is a service for securely managing access to AWS services and resources, enabling control over who can do what."),
            Flashcard("What is the main purpose of load balancing?", "To distribute network traffic across multiple servers",
                      ["To increase server capacity", "To distribute network traffic across multiple servers", "To encrypt data in transit", "To manage database connections"],
                      reason="Load balancers distribute traffic across multiple servers to ensure no server is overwhelmed and to improve fault tolerance."),
            Flashcard("What does IaaS stand for?", "Infrastructure as a Service",
                      ["Internet as a Service", "Integration as a Service", "Infrastructure as a Service", "Information as a Service"],
                      reason="IaaS provides virtualized computing resources over the internet, allowing businesses to scale infrastructure as needed."),
            Flashcard("What is the purpose of a VPC in cloud computing?", "To create a private, isolated section of a cloud",
                      ["To manage virtual machines", "To create a private, isolated section of a cloud", "To provide content delivery", "To store data securely"],
                      reason="VPC allows users to create a private, isolated section of the AWS cloud where they can define their own networking environment."),
            Flashcard("Frequent overwrites, deletes, latest data retrieval - recommended database?","Amazon Relational Database Service (Amazon RDS)",
                    ["Amazon ElastiCache","Amazon Simple Storage Service (Amazon S3)","Amazon Neptune", "Amazon Relational Database Service (Amazon RDS)"],
                    reason="Amazon RDS supports structured data with ACID properties, making it ideal for applications requiring consistent, up-to-date information with frequent modifications."),
            Flashcard("Unencrypted RDS databases - steps for encryption?", 
          "Take a snapshot of the database, copy it as an encrypted snapshot, and restore a database from the encrypted snapshot. Terminate the previous database",
          ["Take a snapshot of the database, copy it as an encrypted snapshot, and restore a database from the encrypted snapshot. Terminate the previous database",
           "Enable Multi-AZ for the database, and make sure the standby instance is encrypted. Stop the main database to that the standby database kicks in, then disable Multi-AZ",
           "Enable encryption on the Amazon RDS database using the AWS Console",
           "Create a Read Replica of the database, and encrypt the read replica. Promote the read replica as a standalone database, and terminate the previous database"],
          reason="You cannot directly encrypt an existing unencrypted Amazon RDS database. The correct approach is to take a snapshot, encrypt it, and restore a new database from that encrypted snapshot."),
          Flashcard("Robust disaster recovery strategy for Amazon ElastiCache Redis with minimal downtime and data loss?", 
          "Opt for Multi-AZ configuration with automatic failover functionality to help mitigate failure",
          ["Schedule manual backups using Redis append-only file (AOF)",
           "Opt for Multi-AZ configuration with automatic failover functionality to help mitigate failure",
           "Schedule daily automatic backups at a time when you expect low resource utilization for your cluster",
           "Add read-replicas across multiple availability zones to reduce the risk of potential data loss because of failure"],
          reason="Opt for Multi-AZ configuration with automatic failover functionality to help mitigate failure - Multi-AZ is the best option when data retention, minimal downtime, and application performance are a priority.\n\nData-loss potential - Low. Multi-AZ provides fault tolerance for every scenario, including hardware-related issues.\n\nPerformance impact - Low. Of the available options, Multi-AZ provides the fastest time to recovery, because there is no manual procedure to follow after the process is implemented.\n\nCost - Low to high. Multi-AZ is the lowest-cost option. Use Multi-AZ when you can't risk losing data because of hardware failure or you can't afford the downtime required by other options in your response to an outage."
            ),
        Flashcard("Improve security of Lambda to RDS PostgreSQL connection with short-lived credentials - recommended actions?", 
          "Attach an AWS Identity and Access Management (IAM) role to AWS Lambda and Use IAM authentication from Lambda to RDS PostgreSQL",
          ["Attach an AWS Identity and Access Management (IAM) role to AWS Lambda",
           "Restrict the RDS database security group to the Lambda's security group",
           "Use IAM authentication from Lambda to RDS PostgreSQL",
           "Embed a credential rotation logic in the AWS Lambda, retrieving them from SSM",
           "Deploy AWS Lambda in a VPC"],
          reason="Attaching an IAM role to AWS Lambda allows Lambda functions to assume permissions needed for accessing RDS PostgreSQL securely. Using IAM authentication from Lambda to RDS PostgreSQL provides short-lived, automatically managed credentials, enhancing security by avoiding hard-coded credentials and reducing risk of credential leakage."
            ),
         Flashcard("Maximize availability for SQL Server database migration to AWS with minimal overhead - recommended approach?", 
          "Migrate the data to Amazon RDS for SQL Server database in a Multi-AZ deployment",
          ["Migrate the data to EC2 instance hosted SQL Server database. Deploy the EC2 instances in a Multi-AZ configuration",
           "Migrate the data to Amazon RDS for SQL Server database in a cross-region read-replica configuration",
           "Migrate the data to Amazon RDS for SQL Server database in a cross-region Multi-AZ deployment",
           "Migrate the data to Amazon RDS for SQL Server database in a Multi-AZ deployment"],
          reason="Amazon RDS for SQL Server with Multi-AZ deployment provides high availability with minimal operational and management overhead by automatically handling failover, backups, and patching. It ensures maximum availability within a single region without the additional complexity of cross-region configurations."
        ),
        Flashcard("Database solution with Auto Scaling, high availability, and continuous data stream capability for IoT - recommended option?", 
          "Amazon DynamoDB",
          ["Amazon Relational Database Service (Amazon RDS)",
           "Amazon Aurora",
           "Amazon DynamoDB",
           "Amazon Redshift"],
          reason="Amazon DynamoDB offers Auto Scaling, high availability, and the ability to handle changes in data attributes over time. It also supports DynamoDB Streams, which provides a continuous stream of changes to the data, making it ideal for IoT applications requiring real-time updates."
        ),
        Flashcard("What is DNS (Domain Name System)?", 
          "DNS translates domain names into IP addresses used by computers to communicate.",
          ["DNS encrypts internet traffic", 
           "DNS provides domain name registration", 
           "DNS translates domain names into IP addresses", 
           "DNS manages server load balancing"],
          reason="DNS is like the internet's address book, translating human-readable domain names (e.g., example.com) into the numeric IP addresses that computers use for communication."
),
Flashcard("What does TTL (Time-to-Live) in DNS specify?", 
          "How long a DNS record should be cached before it needs to be refreshed.",
          ["How long a DNS server remains active", 
           "How long a DNS record should be cached before it needs to be refreshed", 
           "The time it takes for a DNS lookup to complete", 
           "The maximum time a DNS server can store logs"],
          reason="TTL in DNS reduces the frequency of DNS lookups by specifying how long a DNS record can be cached. This improves performance by allowing faster resolution of domain names."
),




          

        ]

def main():
    st.set_page_config(page_title="Sweta's Flashcard App", page_icon="🎓")
    st.title("Data Science and Cloud Computing Flashcards")

    app = FlashcardApp()

    if 'current_cards' not in st.session_state:
        st.session_state.current_cards = []
    if 'current_card' not in st.session_state:
        st.session_state.current_card = None
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'total_questions' not in st.session_state:
        st.session_state.total_questions = 0

    topic = st.radio("Choose a topic:", ("Data Science", "Cloud Computing"))

    if st.button("Start/Reset"):
        if topic == "Data Science":
            st.session_state.current_cards = app.data_science_cards.copy()
        else:
            st.session_state.current_cards = app.cloud_computing_cards.copy()
        st.session_state.show_answer = False
        st.session_state.current_card = None
        st.session_state.score = 0
        st.session_state.total_questions = 0

    if st.session_state.current_cards:
        if st.session_state.current_card is None:
            st.session_state.current_card = random.choice(st.session_state.current_cards)
            st.session_state.show_answer = False

        if st.session_state.current_card:
            st.subheader("Question:")
            st.write(st.session_state.current_card.question)

            if st.session_state.current_card.options:
                user_answer = st.radio("Choose the correct answer:", st.session_state.current_card.options)
                
                col1, col2 = st.columns(2)
                
                with col1:
                    if st.button("Submit Answer"):
                        st.session_state.show_answer = True
                        st.session_state.total_questions += 1
                        if user_answer == st.session_state.current_card.answer:
                            st.session_state.score += 1
                            st.success("Correct!")
                        else:
                            st.error(f"Incorrect. The correct answer is: {st.session_state.current_card.answer}")
                
                with col2:
                    if st.button("Next Card"):
                        st.session_state.current_card = random.choice(st.session_state.current_cards)
                        st.session_state.show_answer = False

            if st.session_state.show_answer:
                st.subheader("Answer:")
                st.write(st.session_state.current_card.answer)
                if st.session_state.current_card.reason:
                    st.write(f"**Reason**: {st.session_state.current_card.reason}")

        st.write(f"Score: {st.session_state.score}/{st.session_state.total_questions}")
    else:
        st.write("Please choose a topic and click 'Start/Reset' to begin.")

if __name__ == "__main__":
    main()
