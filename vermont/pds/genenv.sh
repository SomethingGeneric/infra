#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

# Secure generator comands
GENERATE_SECURE_SECRET_CMD="openssl rand --hex 16"
GENERATE_K256_PRIVATE_KEY_CMD="openssl ecparam --name secp256k1 --genkey --noout --outform DER | tail --bytes=+8 | head --bytes=32 | xxd --plain --cols 32"

PDS_DATADIR="/pds"

[[ ! -d "${PDS_DATADIR}" ]] && mkdir -p "${PDS_DATADIR}"

PDS_DID_PLC_URL="https://plc.directory"
PDS_BSKY_APP_VIEW_URL="https://api.bsky.app"
PDS_BSKY_APP_VIEW_DID="did:web:api.bsky.app"
PDS_REPORT_SERVICE_URL="https://mod.bsky.app"
PDS_REPORT_SERVICE_DID="did:plc:ar7c4by46qjdydhdevvrndac"
PDS_CRAWLERS="https://bsky.network"

# Generate environment variables
printf 'PDS hostname: '
read PDS_HOSTNAME

printf "Admin password: "
read -s PDS_ADMIN_PASSWORD

printf "\nAdmin email: "
read PDS_ADMIN_EMAIL

printf "\nSMTP username: "
read SMTP_USERNAME

printf "SMTP password: "
read -s SMTP_PASSWORD

printf "\nSMTP server (and port): "
read SMTP_SERVER

printf "\nSMTP from address: "
read SMTP_FROM_ADDRESS

cat << EOF > "${PDS_DATADIR}/pds.env"
PDS_HOSTNAME=${PDS_HOSTNAME}
PDS_JWT_SECRET=$(eval "${GENERATE_SECURE_SECRET_CMD}")
PDS_ADMIN_PASSWORD=${PDS_ADMIN_PASSWORD}
PDS_PLC_ROTATION_KEY_K256_PRIVATE_KEY_HEX=$(eval "${GENERATE_K256_PRIVATE_KEY_CMD}")
PDS_DATA_DIRECTORY=${PDS_DATADIR}
PDS_BLOBSTORE_DISK_LOCATION=${PDS_DATADIR}/blocks
PDS_DID_PLC_URL=${PDS_DID_PLC_URL}
PDS_BSKY_APP_VIEW_URL=${PDS_BSKY_APP_VIEW_URL}
PDS_BSKY_APP_VIEW_DID=${PDS_BSKY_APP_VIEW_DID}
PDS_REPORT_SERVICE_URL=${PDS_REPORT_SERVICE_URL}
PDS_REPORT_SERVICE_DID=${PDS_REPORT_SERVICE_DID}
PDS_CRAWLERS=${PDS_CRAWLERS}
PDS_ADMIN_EMAIL=${PDS_ADMIN_EMAIL}
PDS_EMAIL_FROM_ADDRESS="${SMTP_FROM_ADDRESS}"
PDS_EMAIL_SMTP_URL="smtp://${SMTP_USERNAME}:${SMTP_PASSWORD}@${SMTP_SERVER}"
PDS_PORT=3001
LOG_ENABLED=true
EOF