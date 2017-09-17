"""alfred base controller."""

from cement.ext.ext_argparse import ArgparseController, expose

class alfredBaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = 'My Helper in Crime'
        arguments = [
            (['-l', '--length'],
             dict(help='length of generated password', dest='length', action='store',
                  metavar='NUM') ),
            ]

    @expose(hide=True)
    def default(self):
        print("Alfred at your service Master")

    @expose(help="Generate random password")
    def genpass(self):
        print("Sorry Master San! I cannot generate password as of now")

    @expose(help='Generate random text')
    def gentext(self):
        print('Do you mean lorem ipsum text, those are boring text, how about an actual text from a magazine')
