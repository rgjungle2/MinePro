# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart(n)

All the cide is worked correct.

using namespace std;
void bubblesort(int arr[], int n)
{
    if (n == 0 || n == 1)
    {
        return;
    }
    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i] > arr[i + 1])
        {
            swap(arr[i], arr[i + 1]);
        }
    }
    bubblesort(arr, n - 1);
}
int main()
{
    int arr[5] = {2, 5, 1, 6, 9};
    bubblesort(arr, 5);
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
