from G_Parser import Parser

def driver():
    P = Parser()
    P.BuildParser()


    s = r'''
            int x;
            int y;

            float function(y){

            }
         '''
    result = P.Parser.parse(s)
    print(result)

driver()
