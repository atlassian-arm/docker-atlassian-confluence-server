#!/usr/bin/python3 -B

import os, logging

from entrypoint_helpers import env, gen_cfg, str2bool, start_app

def create_dir(path):
    try:
        os.mkdir(path)
        os.chown(path, int(env['run_uid']), int(env['run_gid']))
        logging.info(f"Created directory {path}")
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

RUN_USER = env['run_user']
RUN_GROUP = env['run_group']
CONFLUENCE_INSTALL_DIR = env['confluence_install_dir']
CONFLUENCE_HOME = env['confluence_home']

gen_cfg('server.xml.j2', f'{CONFLUENCE_INSTALL_DIR}/conf/server.xml')
gen_cfg('seraph-config.xml.j2',
        f'{CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/classes/seraph-config.xml')
gen_cfg('confluence-init.properties.j2',
        f'{CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/classes/confluence-init.properties')
gen_cfg('confluence.cfg.xml.j2', f'{CONFLUENCE_HOME}/confluence.cfg.xml',
        user=RUN_USER, group=RUN_GROUP, overwrite=False)

if str2bool(env.get('confluence_log_stdout')):
        create_dir(f'{CONFLUENCE_HOME}/logs')
        tee_command = f'| tee {CONFLUENCE_HOME}/logs/atlassian-confluence.log'

start_app(f'{CONFLUENCE_INSTALL_DIR}/bin/start-confluence.sh -fg {tee_command}', CONFLUENCE_HOME, name='Confluence')
