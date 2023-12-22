resource "aws_iam_role" "hello_lamda_exec" {
  name = "hello-lamda"

  assume_role_policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Action": "sts:AssumeRole",
        "Principal": {
            "Service": [
            "lambda.amazonaws.com"
            ]
        },
        "Effect": "Allow",
        "Sid": ""
        }
    ]
}
POLICY
}

resource "aws_iam_role_policy_attachment" "hello_lamda_policy" {
  role = aws_iam_role.hello_lamda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "hello" {
    function_name = "hello"
    role = aws_iam_role.hello_lamda_exec.arn

    s3_bucket     = aws_s3_bucket.lambda_bucket.id
    s3_key        = aws_s3_object.lambda_hello.key

    runtime = "nodejs16.x"
    handler = "function.handler"

    source_code_hash = data.archive_file.lambda_hello.output_base64sha256
}

resource "aws_cloudwatch_log_group" "hello" {
    name = "/aws/lamda/${aws_lambda_function.hello.function_name}"

    retention_in_days = 14
}

data "archive_file" "lambda_hello" {
    type = "zip"

    source_dir = "../${path.module}/hello"
    output_path = "../${path.module}/hello.zip"
}

resource "aws_s3_object" "lambda_hello" {
    bucket = aws_s3_bucket.lambda_bucket.id

    key = "hello.zip"
    source = data.archive_file.lambda_hello.output_path

    etag = filemd5(data.archive_file.lambda_hello.output_path)
  
}