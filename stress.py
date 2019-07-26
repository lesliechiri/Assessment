
import click


@click.command()
@click.option('--first' ,prompt = 'firstname')
@click.option('--second' ,prompt = 'secondname')



def initials(first,second):
    if first:
        x = first[0]
    if second:
        y = second[0]

        z= x+y    

   
    

        click.echo(z)

    

if __name__ == '__main__':

    initials()