☁️ AWS Cost Optimization Automation System

Serverless automation to detect unused AWS resources and reduce cloud costs — zero manual effort!

📌 About the Project

This project automates the process of identifying and cleaning up unused oridle AWS resources using a fully serverless architecture. It runs daily, validates resources before taking any action, sends alerts, and displays savings on a dashboard — all without any human intervention.

✨ Features


🔍 Detects unused EC2 instances (stopped/idle)
💾 Finds unattached EBS volumes
🪣 Identifies empty or unused S3 buckets
📸 Flags old RDS snapshots (older than 30 days)
⚖️ Validates resources before deletion (age, tags, usage, business hours)
📧 Sends automated alerts via Email, Slack, or Teams
📊 Visualizes savings on Amazon QuickSight dashboard
🔒 Secure & controlled — uses IAM least privilege access
🏷️ Tag-based protection — excludes critical resources from cleanup
⚙️ Fully automated — runs daily via EventBridge scheduler

<img width="1100" height="800" alt="aws_cost_optimization_architecture (1)" src="https://github.com/user-attachments/assets/c945d30b-b2eb-4c47-a34d-6cbc1a1c6d7d" />

📁 Project Structure

aws-cost-optimization-system/
├── 📁 src/
│   ├── cost_optimizer.py       # Main Lambda handler
│   ├── ec2_cleaner.py          # EC2 resource management
│   ├── ebs_cleaner.py          # EBS volume management
│   ├── s3_cleaner.py           # S3 bucket management
│   └── sns_notifier.py         # Alert notifications
├── 📁 policies/
│   ├── iam_policy.json         # Main IAM permissions
│   ├── trust_policy.json       # Lambda trust policy
│   ├── eventbridge_policy.json # EventBridge permissions
│   └── cloudwatch_policy.json  # Logging permissions
├── 📁 docs/
│   └── aws_cost_optimization_architecture.jpg
├── .gitignore
├── requirement.txt
└── README.md

⚙️ How It Works

Every day at 8 AM IST
         ↓
EventBridge triggers Lambda
         ↓
Lambda scans all AWS resources
         ↓
Validation logic checks each one
  ├── Age check
  ├── Usage check
  ├── Tag / exclusion rules
  └── Business hours check
         ↓
Safe to clean? → Delete / Stop + Log it
         ↓
SNS sends summary report (Email/Slack)
         ↓
CloudWatch stores all logs
         ↓
QuickSight updates savings dashboard


🚀 Resources Discovered & Cleaned

ResourceConditionActionEC2 InstancesStopped / IdleStop or TerminateEBS VolumesUnattachedDeleteS3 BucketsEmpty / UnusedDeleteRDS SnapshotsOlder than 30 daysDeleteElastic Load BalancersNo trafficDeleteElastic IPsUnattachedRelease


🔐 Security


✅ IAM Least Privilege — Lambda only has permissions it needs
✅ Tag Protection — Tag any resource with exclude:true to skip it
✅ Validation before deletion — nothing is deleted without passing all checks
✅ Business hours check — avoids running during peak production hours
✅ CloudWatch logging — every action is logged and traceable



📦 Installation & Setup

1. Clone the repository

bashgit clone https://github.com/ughade-prathmesh/aws-cost-optimization-system.git
cd aws-cost-optimization-system

2. Install dependencies

bashpip install -r requirement.txt

3. Configure AWS CLI

bashaws configure

4. Deploy Lambda function

bashcd src
zip function.zip cost_optimizer.py ec2_cleaner.py ebs_cleaner.py s3_cleaner.py sns_notifier.py

aws lambda create-function \
  --function-name cost-optimizer \
  --runtime python3.11 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/cost-optimizer-role \
  --handler cost_optimizer.lambda_handler \
  --zip-file fileb://function.zip \
  --timeout 300

5. Setup EventBridge daily trigger

bashaws events put-rule \
  --name daily-cost-check \
  --schedule-expression "cron(30 2 * * ? *)" \
  --state ENABLED

6. Setup SNS email alerts

bashaws sns create-topic --name cost-alerts

aws sns subscribe \
  --topic-arn arn:aws:sns:ap-south-1:YOUR_ACCOUNT_ID:cost-alerts \
  --protocol email \
  --notification-endpoint your@email.com


📊 Key Benefits

Without This SystemWith This SystemPay for unused resourcesOnly pay for what you useManual checking requiredFully automated daily scanNo visibility on wasteDashboard shows all savingsRisk of human errorValidated before every actionNo alertsReal-time email/Slack alerts

👨‍💻 Author

Prathmesh Ughade
