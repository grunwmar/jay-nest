""" Jay nest """

class Jay:
    """ Jay servers for quict inspection of object in code when """
    """ coder is interested in its value on specific place. """
    """ When called with IO object like stream or file, Jay's message is writen """
    """ to IO object. When IO is not specified, message us just printed. """


    def __init__(self, stream=None):
        self._stream = stream
        self._message = "{value} {type}" # default string

    def __getitem__(self, message):
        """ Allows to change messagge format (replace default). """
        self._message = message
        return self

    def __ror__(self, object):
        """ Takes preceeding object and check its str() and type() to use them """
        """ to fill its values to message template and write/print message."""
        """ Then preceedig object is set as return value of this method """
        """ so object behaves like pipe with a detector. """
        t = repr(type(object))
        t_name = type(object).__name__
        v = repr(object)

        msg = self._message.format(value=v, typename=t_name, type=t)

        if self._stream is None:
            print("[🐦»",msg,"]")
        else:
            self._stream.write(msg + "\n")
        return object
