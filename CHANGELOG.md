# Change Log
All notable changes to this project will be documented in this file.

## [1.5.0] - 2017-03-09
### Added
- Compatability with Xolphin REST Api v1.5.0
- Request Notes: You are able to get all and send your own request notes
- Certificate Requests: If there are open request notes for the customer, a new field 'requiresAction' will be set in the CertificateRequest object
- Certificate Requests: You can now send a language parameter with the request, which will be used for (eg) the Subscriber Agreement
- Certificate Requests: A new field 'brandValidation' is added, which is used to indicate if the request is being held for review due to specific brand names

### Fixed
- Ability to upload files