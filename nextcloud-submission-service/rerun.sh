sudo docker build -t nextcloud_submission_service .
sudo docker stop nextcloud_submitter
sudo docker rm nextcloud_submitter
sudo docker run --name nextcloud_submitter -p 80:80 nextcloud_submission_service