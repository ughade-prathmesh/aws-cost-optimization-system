# ☁️ AWS Cost Optimization Automation System

> **Serverless automation to detect unused AWS resources and reduce cloud costs — zero manual effort!**

---

## 📌 About the Project

This project automates the process of identifying and cleaning up unused or idle AWS resources using a fully serverless architecture. It runs daily, validates resources before taking any action, sends alerts, and displays savings on a dashboard — all without any human intervention.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 EC2 Detection | Finds stopped or idle EC2 instances |
| 💾 EBS Cleanup | Detects unattached EBS volumes |
| 🪣 S3 Cleanup | Identifies empty or unused S3 buckets |
| 📸 RDS Snapshots | Flags old snapshots older than 30 days |
| ⚖️ Validation | Checks age, tags, usage before deletion |
| 📧 Alerts | Sends reports via Email, Slack, or Teams |
| 📊 Dashboard | Visualizes savings on Amazon QuickSight |
| 🔒 Secure | Uses IAM least privilege access |
| 🏷️ Tag Protection | Excludes critical resources from cleanup |
| ⚙️ Automated | Runs daily via EventBridge scheduler |

---

## 🏗️ Architecture

| Step | Service | Role |
|------|---------|------|
| 1 | Amazon EventBridge | Triggers Lambda daily at 8 AM IST |
| 2 | AWS Lambda (Python + Boto3) | Main automation engine |
| 3 | Resource Discovery | Scans EC2, EBS, S3, RDS, ELB |
| 4 | Validation Logic | Age check, tag rules, usage check |
| 5 | Automated Actions | Stop EC2, delete EBS / S3 / snapshots |
| 6 | Amazon CloudWatch | Logs, metrics, error tracking |
| 7 | Amazon SNS | Email / Slack / Teams alerts |
| 8 | Amazon QuickSight | Cost savings dashboard |



<img width="1100" height="800" alt="aws_cost_optimization_architecture (1)" src="https://github.com/user-attachments/assets/6a9d0c3f-3ff7-403d-9eea-e6f23cec97ab" />

---

## 📁 Project Structure

```
aws-cost-optimization-system/
├── src/
│   ├── cost_optimizer.py         # Main Lambda handler
│   ├── ec2_cleaner.py            # EC2 resource management
│   ├── ebs_cleaner.py            # EBS volume management
│   ├── s3_cleaner.py             # S3 bucket management
│   └── sns_notifier.py           # Alert notifications
├── policies/
│   ├── iam_policy.json           # Main IAM permissions
│   ├── trust_policy.json         # Lambda trust policy
│   ├── eventbridge_policy.json   # EventBridge permissions
│   └── cloudwatch_policy.json    # Logging permissions
├── docs/
│   └── aws_cost_optimization_architecture.jpg
├── .gitignore
├── requirement.txt
└── README.md
```

---

## ⚙️ How It Works

```
Every day at 8 AM IST
         |
         v
EventBridge triggers Lambda
         |
         v
Lambda scans all AWS resources
         |
         v
Validation logic checks each one
  |-- Age check
  |-- Usage check
  |-- Tag / exclusion rules
  |-- Business hours check
         |
         v
Safe to clean? --> Delete / Stop + Log it
         |
         v
SNS sends summary report (Email / Slack)
         |
         v
CloudWatch stores all logs
         |
         v
QuickSight updates savings dashboard
```

---

## 🚀 Resources Discovered and Cleaned

| Resource | Condition | Action |
|----------|-----------|--------|
| EC2 Instances | Stopped or Idle | Stop or Terminate |
| EBS Volumes | Unattached | Delete |
| S3 Buckets | Empty or Unused | Delete |
| RDS Snapshots | Older than 30 days | Delete |
| Elastic Load Balancers | No traffic | Delete |
| Elastic IPs | Unattached | Release |

---

## 🔐 Security

| Security Feature | Details |
|-----------------|---------|
| IAM Least Privilege | Lambda only has the permissions it needs |
| Tag Protection | Tag any resource with `exclude:true` to skip it |
| Validation Before Deletion | Nothing is deleted without passing all checks |
| Business Hours Check | Avoids running during peak production hours |
| CloudWatch Logging | Every action is logged and traceable |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Core programming language |
| Boto3 | AWS SDK for Python |
| AWS Lambda | Serverless compute |
| Amazon EventBridge | Daily scheduling |
| Amazon SNS | Notifications and alerts |
| Amazon CloudWatch | Logging and monitoring |
| Amazon QuickSight | Cost dashboard |
| AWS IAM | Access control and security |

---

## 📦 Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/ughade-prathmesh/aws-cost-optimization-system.git
cd aws-cost-optimization-system
```

**2. Install dependencies**

```bash
pip install -r requirement.txt
```

**3. Configure AWS CLI**

```bash
aws configure
```

**4. Deploy Lambda function**

```bash
cd src
zip function.zip cost_optimizer.py ec2_cleaner.py ebs_cleaner.py s3_cleaner.py sns_notifier.py

aws lambda create-function \
  --function-name cost-optimizer \
  --runtime python3.11 \
  --role arn:aws:iam::YOUR_ACCOUNT_ID:role/cost-optimizer-role \
  --handler cost_optimizer.lambda_handler \
  --zip-file fileb://function.zip \
  --timeout 300
```

**5. Setup EventBridge daily trigger**

```bash
aws events put-rule \
  --name daily-cost-check \
  --schedule-expression "cron(30 2 * * ? *)" \
  --state ENABLED
```

**6. Setup SNS email alerts**

```bash
aws sns create-topic --name cost-alerts

aws sns subscribe \
  --topic-arn arn:aws:sns:ap-south-1:YOUR_ACCOUNT_ID:cost-alerts \
  --protocol email \
  --notification-endpoint your@email.com
```

---

## 📊 Key Benefits

| Without This System | With This System |
|---------------------|-----------------|
| Pay for unused resources | Only pay for what you use |
| Manual checking required | Fully automated daily scan |
| No visibility on waste | Dashboard shows all savings |
| Risk of human error | Validated before every action |
| No alerts | Real-time Email and Slack alerts |
| Resources pile up silently | Cleaned up automatically every day |

---

## 🤝 Contributing

Contributions are welcome!

- Star this repository
- Report bugs via Issues
- Submit Pull Requests

---

## 👨‍💻 Author

**Prathmesh Ughade**

GitHub : [ughade-prathmesh](https://github.com/ughade-prathmesh)

---

## 📄 License

This project is open source and available under the MIT License.

---

If this project helped you, please give it a star!
