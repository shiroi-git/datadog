resource "aws_instance" "example" {
  subnet_id     = "subnet-0df56e7cfed24fe54"
  ami           = "ami-0053d11f74e9e7f52"
  instance_type = "t3.micro"
}
