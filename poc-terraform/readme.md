cd terraform
terraform init
terraform apply

aws lambda invoke --region=us-east-1 --function-name=hello response.json