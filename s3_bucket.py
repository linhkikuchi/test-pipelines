#!/usr/bin/env python3
import boto3
import sys
import re
from botocore.exceptions import ClientError, NoCredentialsError

def delete_s3_bucket(bucket_name, region='us-east-1'):
    """Delete an S3 bucket and all its contents"""
    try:
        s3_client = boto3.client('s3', region_name=region)
        s3_client.delete_bucket(Bucket=bucket_name)
        
        print(f"Successfully deleted bucket: {bucket_name}")
        return True
        
    except ClientError as e:
        print(f"Error deleting bucket {bucket_name}: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error deleting bucket {bucket_name}: {e}")
        return False

def list_buckets_with_pattern(customer_name, env_name, region='us-east-1'):
    try:
        s3_client = boto3.client('s3', region_name=region)
        response = s3_client.list_buckets()
        pattern = f"{customer_name}_{env_name}"
        
        matching_buckets = []
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            if pattern in bucket_name:
                matching_buckets.append(bucket_name)
        
        return matching_buckets
        
    except Exception as e:
        print(f"Error listing buckets: {e}")
        return []

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Delete S3 buckets with specific pattern')
    parser.add_argument('--customer-name', required=True, help='Customer name')
    parser.add_argument('--env-name', required=True, help='Environment name')
    parser.add_argument('--region', default='us-east-1', help='AWS region')
    parser.add_argument('--dry-run', action='store_true', help='List buckets without deleting')
    args = parser.parse_args()
    
    customer_name = input("Enter customer name: ")
    env_name = input("Enter environment name: ")
    region = input("Enter AWS region (default: us-east-1): ") or 'us-east-1'
    
    print(f"Searching for buckets matching pattern: {customer_name}_{env_name}")
    
    # List matching buckets
    matching_buckets = list_buckets_with_pattern(customer_name, env_name, region)
    
    if not matching_buckets:
        print("No buckets found matching the pattern")
        return
    
    print(f"Found {len(matching_buckets)} buckets:")
    for bucket in matching_buckets:
        print(f"  - {bucket}")
    
    confirm = input(f"\nAre you sure you want to delete {len(matching_buckets)} buckets? (y/N): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled")
        return
    
    # Delete buckets
    deleted_count = 0
    failed_count = 0
    
    for bucket in matching_buckets:
        if delete_s3_bucket(bucket, region):
            deleted_count += 1
        else:
            failed_count += 1
    print(f"  Successfully deleted: {deleted_count}")
    print(f"  Failed to delete: {failed_count}")
    print(f"\nDeletion completed. Deleted: {deleted_count}, Failed: {failed_count}")

if __name__ == "__main__":
    main()
