import docker
import argh

@argh.arg('container', help='container name')
def cmdline(container):
    d = docker.client.Client()

    cont = d.inspect_container(container)
    config = cont['Config']

    environment = []
    envs = ' '.join(['-e '+env for env in config['Env']])
    volumes = ' '.join(['-v {}:{}'.format(external, internal) for internal, external in cont['Volumes'].items()])
    memory = config['Memory']
    cpu_shares = config['CpuShares']
    workdir = config['WorkingDir']
    cmd = ' '.join(config['Cmd'])
    image = config['Image']

    return 'docker run {envs} {volumes} -m {memory} -c {cpu_shares} -w {workdir} -P --rm -t -i {image} {cmd}'.format(**locals())

def main():
    argh.dispatch_command(cmdline)
