import xolphin
client = xolphin.Client('youremail@domain.com', 'YourPassword', True);

product = 147
years = 1
csr = """-----BEGIN CERTIFICATE REQUEST-----
MIICszCCAZsCAQAwbjELMAkGA1UEBhMCR0IxDzANBgNVBAgMBkxvbmRvbjEPMA0G
A1UEBwwGTG9uZG9uMRMwEQYDVQQKDApTU0wyNDcgTHRkMQswCQYDVQQLDAJJVDEb
MBkGA1UEAwwSc3NsMjQ3LXRlc3RpbmcuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC
AQ8AMIIBCgKCAQEAwkpLdjQJohfnqBoNXCMTnsOaXfyz7a4nm3BNZhGF9I4fPdd9
fuOZhOqIdy2tmQUp82rm9OjDtj9NjJHD3YRGLwTUJ2CJfCIaKescGAZYe8iNNyJ8
Fuw/Jc2TD6UKgb/HyD9grqMQEPojD469ZA8ZYjAPax8UsilTdU5a8w0F+U6uF7Q+
IMlo/OZ5pqewQTZ/fqPm/MoGiUYnMEnSzE9aVGUSjMov8nd/s/pEbM3Je7zg4aHX
gFemBN5GY8vFQanZhSvGcIhhjdK3ac7Q5j5Y20sYmaORulvz0YH40ZYoml8KP8GO
PKOlLhpKnade4u+kxo72Ws05cRtm4N78B5JLsQIDAQABoAAwDQYJKoZIhvcNAQEL
BQADggEBADNQWLy+z8HdN3Xz0HJAPK6c5G7ukCAu/P8sYwNkWFnGGBrY7Uvl3XXF
vSBMWS04AzylTn2qqHKuz5dIq68lgi0CTl1tR2Sp8/5vwCFZntJHGG6f/L/DRKcL
Iriu7QW4mi5dQpDX6maJu/lE38XrcX/r2QdCkCWskiOdh+EnpwibdfT7sVqSrvDh
Cgd0E7WtG1ecGB1QTpCsHBHMk604Pj/wDnw5SvNoX01dm8n3PY5/UfMFVrCnx2uT
VDiArcp4X9/aZCiJxrf6UzY/7FH6qXYiP+hlIVqrqZ7Y3qaFQznBO3VWWNvuunXd
1V2zpjfQjv+FuBDHyKUgX0Q4h3M9XTw=
-----END CERTIFICATE REQUEST-----"""
dcv_type = "DNS"


ov_request = client.request().create(product,years,csr,dcv_type)

ov_request.approver_representative_first_name = 'FirstName'
ov_request.approver_representative_last_name = 'LastName'
ov_request.approver_representative_position = 'Position'
ov_request.approver_representative_phone = '+12345678901'
ov_request.approver_representative_email = 'approver@emailaddress.com'
ov_request.city = 'London'
ov_request.zipcode = 'EC1R 0JH'
ov_request.address = '3/11 Pine Street'
ov_request.subject_alternative_names.append('test1.ssl247-testing.com')
ov_request.subject_alternative_names.append('test2.ssl247-testing.com')
ov_request.dcvType = 'DNS'

#print(ov_request.toDict());

request = client.request().send(ov_request)

print(vars(request))
