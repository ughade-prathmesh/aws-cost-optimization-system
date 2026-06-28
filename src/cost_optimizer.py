import json
import os
from ec2_cleaner import find_stopped_ec2
from ebs_cleaner import find_unused_ebs
from s3_cleaner import find_empty_buckets
from sns_notifier import send_alert

SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN", "")
if not SNS_TOPIC_ARN:
    raise ValueError("Missing env var SNS_TOPIC_ARN")

def lambda_handler(event, context):
    """Main Lambda handler - entry point"""
    print("🚀 Starting AWS Cost Optimization...")
    
    all_findings = []
    
    # 1. Check EC2
    ec2_issues = find_stopped_ec2()
    for i in ec2_issues:
        all_findings.append({
            'type': 'Stopped EC2 Instance',
            'id': i['InstanceId'],
            'action': 'Review and Terminate if not needed'
        })
    
    # 2. Check EBS
    ebs_issues = find_unused_ebs()
    for i in ebs_issues:
        all_findings.append({
            'type': 'Unattached EBS Volume',
            'id': i['VolumeId'],
            'action': 'Delete if not needed'
        })
    
    # 3. Check S3
    s3_issues = find_empty_buckets()
    for i in s3_issues:
        all_findings.append({
            'type': 'Empty S3 Bucket',
            'id': i['BucketName'],
            'action': 'Delete if not needed'
        })
    
    print(f"📊 Total Issues Found: {len(all_findings)}")
    
    # 4. Send Report
    if all_findings:
        send_alert(all_findings, SNS_TOPIC_ARN)
    else:
        print("✅ No issues found! Your AWS is clean.")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Cost optimization complete!',
            'total_issues': len(all_findings),
            'findings': all_findings
        })
    }