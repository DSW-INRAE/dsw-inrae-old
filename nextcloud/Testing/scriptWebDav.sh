#man de curl https://linux.die.net/man/1/curl

# Création d'un folder

#curl -u sqmqMHzj83zPP6T:qCxDZNM6 -X MKCOL "https://nextcloud.inrae.fr/public.php/webdav/temp"

# Supréssion d'un folder

#curl -u sqmqMHzj83zPP6T:qCxDZNM6 -X DELETE "https://nextcloud.inrae.fr/public.php/webdav/temp/test.txt"

# Upload un fichier

#curl -u sqmqMHzj83zPP6T:qCxDZNM6 -X PUT "https://nextcloud.inrae.fr/public.php/webdav/temp/" -T "{test.txt, test2.txt}"

#

curl --location --request PUT 'https://nextcloud.inrae.fr/public.php/webdav/temp' \
--header 'Content-Type: image/png' \
--header 'Authorization: Basic c3FtcU1Iemo4M3pQUDZUOnFDeERaTk02' \
--header 'Cookie: SERVERID=nextcloud3-tls.stockage.inra.fr; __Host-nc_sameSiteCookielax=true; __Host-nc_sameSiteCookiestrict=true; oc_sessionPassphrase=61%2F5Ao88uUf6CdVy2e6sGx4YYM3KKNPVIR7QBenNQF%2F065X4%2BrGqEZnhZeKtyYcmGVPybmb3BrQFA%2F2Y9LP%2FSGsgSy0CdUj6vpgdhHs8%2BpfN6WBroegyN%2B3b2ikfTlgk; ocr4hnlcfib7=fd5cfb99dfbcb0b2c965f0a9b2cc70ce' \
-T '/home/theodore/Development/extension-dsw-inrae/nextcloud/Testing/test2.txt'