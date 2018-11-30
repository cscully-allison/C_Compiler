#include <stdio.h>

int ReadInt()
{
	int ReadIn;
	scanf ("%d", &ReadIn);
	return ReadIn;
}

void WriteInt(int ToWrite)
{
	printf ("%d\n", ToWrite);
}

float ReadFloat()
{
	float ReadIn;
	scanf("%f", &ReadIn);
	return ReadIn;
}

void WriteFloat(float ToWrite)
{
	printf ("%f\n", ToWrite);
}

char ReadChar()
{
	char ReadIn;
	scanf("%c", &ReadIn);
	return ReadIn;
}

char WriteChar(char ToWrite)
{
	printf("%c\n", ToWrite);
}