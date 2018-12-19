int main(int arg1)
{
	int arr1[5];
	int arr2[5][7];

	arr1[3]=3;
	arr2[3][6] = arr1[3];
	arr1[2] = arr2[3][6];
}
