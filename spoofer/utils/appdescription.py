from . import logger

description = """  Email-impersonation vulnerability test
  Nebulousltd.com"""

def print_description():
    logger.bright('\n{0}'.format('='*50))
    logger.header(description)
    logger.bright('{0}\n'.format('='*50))


