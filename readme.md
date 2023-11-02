# Xolphin API wrapper for Python
xolphin-python-api is a library which allows quick integration of the [Xolphin REST API](https://api.xolphin.com) in Python to automated ordering, issuance and installation of SSL Certificates.

## About Xolphin
[Xolphin](https://www.xolphin.nl/) is the largest supplier of [SSL Certificates](https://www.sslcertificaten.nl) and [Digital Signatures](https://www.digitalehandtekeningen.nl) in the Netherlands. Xolphin has  
a professional team providing reliable support and rapid issuance of SSL Certificates at an affordable price from industry leading brands such as Comodo, GeoTrust, GlobalSign, Thawte and Symantec.

## Library installation

Library can be installed via [pip](https://pypi.python.org/pypi/pip)

```
pip install xolphin-api
```

And updated via

```
pip install xolphin-api --upgrade
```

Or manually from source

```
git clone https://github.com/xolphin/xolphin-api-python.git
cd xolphin-api-python
python setup.py install
```

## Usage

### Client initialization

```python
import xolphin

client = xolphin.Client('<username>', '<password>')
```

### Requests

#### Getting list of requests

```python
requests = client.request().all()
for request in requests:
    print(request.id, request.product.id)
```

#### Getting request by ID

```python
request = client.request().get(961992637)
print(request.product.brand)
```

#### Request certificate

```python
ccr = client.request().create(24, 1, 'csr string', 'EMAIL')
ccr.address = 'Address'
ccr.approver_representative_first_name = 'FirstName'
ccr.approver_representative_last_name = 'LastName'
ccr.approver_representative_phone = '+12345678901'
ccr.approver_representative_email = 'approver_email@domain.com'
ccr.approver_representative_position = 'Pos'
ccr.approver_email = 'admin@domain.com'
ccr.zipcode = '123456'
ccr.city = 'City'
ccr.company = 'Company'
# currently available languages: en, de, fr, nl
ccr.language = 'en'
ccr.subject_alternative_names.append('test1.domain.com')
ccr.subject_alternative_names.append('test2.domain.com')
ccr.dcv.append({
    'domain': 'test1.domain.com',
    'dcvType': 'EMAIL',
    'approverEmail': 'email@domain.com'
})

request = client.request().send(ccr)
print(request.id)
```

#### Create a note

```python
result = client.request().send_note(1234, 'My message')
print(result.message);
```

#### Get list of notes

```python
result = client.request().get_notes(1234)

for note in result:
    print(note.messageBody);
```

#### Request an "Encryption Everywhere" certificate
```python
ccr = client.request().create_ee()
ccr.csr = "<csr_string>"
ccr.approver_representative_first_name = 'FirstName'
ccr.approver_representative_last_name = 'LastName'
ccr.approver_representative_phone = '+12345678901'
ccr.approver_representative_email = 'approver_email@domain.com'
ccr.approver_representative_position = 'Pos'
ccr.approver_email = 'admin@domain.com'
ccr.subject_alternative_names.append('test1.domain.com')
ccr.subject_alternative_names.append('test2.domain.com')
ccr.dcvType = 'DNS'
request = client.request().send_ee(ccr)
```

#### Send a "Comodo Subscriber Agreement" email

```python
//currently available languages: en, de, fr, nl
result = client.request().send_ComodoSA(124, 'test@example.com')
print(result.message);
```

#### Request Callback (OV and EV certificates)

```python
vc = client.request().configure_validation_call(order_id)
vc.date = "2024-01-26"
vc.time = "11:00"
vc.timezone = "Europe Amsterdam"
vc.phoneNumber = "132456789"
request = client.request().send_validation_call(vc)
```
### Certificate

#### Certificates list and expirations

```python
certificates = client.certificate().all()
for certificate in certificates:
    print(certificate.id, certificate.isExpired())
```

#### Download certificate

```python
cert = client.certificate().download(961983489, 'CRT')
with open('crt.crt', 'wb') as f:
    f.write(cert)
```

### Support

#### Products list

```python
products = client.support().products()
for product in products:
    print(product.id, product.brand)
```

#### Decode CSR

```python
data = client.support().decode_csr('csr string')
print(data.type, data.size)
```
