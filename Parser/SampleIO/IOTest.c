#include "SampleIO.h"

int main()
{
	int a;
	float b;
	char c;

	c = ReadChar();
	b = ReadFloat();
	a = ReadInt();
	WriteInt(a);
	WriteFloat(b);
	WriteChar(c);

	return 0;
}