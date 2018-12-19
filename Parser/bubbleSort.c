int PrintInt(int);
char PrintChar(char);

int main()
{
	int vals[10];
	int a;
	int b;
	int c;

	int next;

	for (a = 0; a < 10; a++)
	{
		vals[a] = 10 - a;
	}

	for (a=0; a < 10; a++)
	{

		for (b=0; b < 9; b++)
		{
			next = b + 1;
			if (vals[b] > vals[next])
			{

				c = vals[b];
				vals[b] = vals[next];
				vals[next]= c;
			}
		}
	}

	//post sort print
	for (a=0; a<10; a++)
	{
		PrintInt(vals[a]);
		PrintChar('-');
	}
}
