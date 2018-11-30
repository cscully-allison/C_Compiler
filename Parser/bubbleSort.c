int main()
{
	int a;
	int b;
	int vals[10];
	int c;

	for (a=0; a<10; a++)
	{

		for (b=0; b<9; b++)
		{
			if (vals[b] > vals[b + 1])
			{

				c = vals[b];
				vals[b] = vals[b + 1];
				vals[b + 1]= c;
			}
		}
	}
}