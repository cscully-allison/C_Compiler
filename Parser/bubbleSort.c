int main()
{
	int a;
	int b;
	int vals[10];
	int c;
	int d;

	for (a=0; a<10; a++)
	{

		for (b=0; b<9; b++)
		{
			d = b + 1;
			if (vals[b] > vals[d])
			{

				c = vals[b];
				vals[b] = vals[d];
				vals[d]= c;
			}
		}
	}
}