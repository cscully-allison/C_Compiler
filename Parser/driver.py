from G_Parser import Parser


def driver():
    P = Parser()
    P.BuildParser()


    s = r'''
            int y = 1;

            int main(){
                y = 2;
            }

         '''
    result = P.Parser.parse(s)
    print(result)

driver()
