# DVC-Versioning-Data

* Create a git repo and clone it in local
* Create code file and add code to it
* Do a git add-commit-push.
* pip install dvc
* Now we do `dvc init` (creates .dvcignore, .dvc)
* In Dvc we have to add the remote repository where we want to store the vwersions of data, for that we have to add the location of this remote laocation using the dvc `remote add -d myremote S3` here S3 is link of remote link of S3 bucket.
* `dvc add data/`  Here  we are telling the dvc to track the data in `data`  folder
*
