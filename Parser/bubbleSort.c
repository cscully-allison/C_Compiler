int main()
{
	int vals[3];
	int a;
	int b;
	int c;
	int next;

	for (a = 0; a < 3; a++)
	{
		vals[a] = 3 - a;
	}


	for (a=0; a < 3; a++)
	{

		for (b=0; b < 2; b++)
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
}
