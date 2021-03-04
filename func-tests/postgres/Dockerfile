FROM postgres:10.16-alpine

# NOTE: This expects the license to have been injected; see
# `inject-license` and INJECT_LICENSE_HERE in `confluence.sql.tmpl`
COPY  confluence.sql /docker-entrypoint-initdb.d/confluence.sql
