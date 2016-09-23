"""
Parse every FASTA record from stdin and print each.
"""

class FASTAReader( object ):
    def __init__( self, file ):
        self.file = file
        self.last_id = None
        
    def __iter__( self ):
        return self
        
    def next( self ):
        if self.last_id is None:
            line = self.file.readline()
            if line == "":
                raise StopIteration
            # Verify is header line
            assert line.startswith( ">" )
            # Extract id -- whole line
            ## identifier = line[1:].rstrip( "\r\n" )
            # Extract id -- space
            identifier = line[1:].split()[0]
        else:
            identifier = self.last_id

        sequences = []

        while True:
            line = self.file.readline().rstrip("\r\n")
            if line.startswith( ">" ):
                self.last_id = line[1:].split()[0]
                break
            elif line == "":
                if sequences:
                    return identifier, "".join( sequences )
                ## return None, None
                raise StopIteration
            else:
                sequences.append( line )
                
        return identifier, "".join( sequences )
    
    
    
    
