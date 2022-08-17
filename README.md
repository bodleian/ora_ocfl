# ora_ocfl
The ORA OCFL project home, for the interactions between Hyrax and OCFL.

The ORA4 Digital Preservation Solution (ORA4 DPS) project aims to store copies of all significant versions of ORA objects in an OCFL storage root.

This project is likely to have two components:
- ocfld: a REST-based OCFL client daemon that is a wrapper around an existing OCFL command line client
- ora-ocfl-worker: a Ruby/Sidekiq worker powered by a redis queue - responsible for communication between Hyrax and ocfld

Contents:

- On Github: the user story-backed issues that will inform client development, 
- /openapi: the OpenAPI API documentation for the proposed ocfld REST-based OCFL daemon
- /test_code: working test code for the ORA4 DPS
- /storage_root: an OCFL-valid storage root containing sample ORA objects in OCFL
- ORA4 Hyrax OCFL connector.pdf - a presentation documenting
  - the proposed ORA4 Review/ORA4 DPS architecture
    - the role of the ocfld REST-based OCFL client
    - the role of the ora-ocfl-worker
  - the user stories behind the Github issues for client development
- ORA4 objects in OCFL.pdf - a document describing how ORA4 objects will be stored in OCFL (including how file purges will be managed)


