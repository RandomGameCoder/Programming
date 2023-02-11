import java.util.Scanner;
class quicksortdemo{
    public static void main(String[] args){
        int n;
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the no of elements ");
        n=sc.nextInt();
        String a[]=new String[n+1];
        System.out.println("Enter the elements");
        int i=0;
        while(i<n+1){
            a[i]=sc.nextLine();
            i++;
        }
        quicksort(a,1,n);
        System.out.println("The string is:");
        for(i=1;i<n+1;i++){
            System.out.print(a[i]+" ");
        }
        System.out.println();
    }

    static void Swap(String arr[],int i,int j){
        String temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    }

    static void quicksort(String arr[],int left,int right){
        if(left<right){
            int i=left,j=right+1;
            String pivot=arr[left];
            do{
                do{i++;} while(i!=right+1 && arr[i].compareTo(pivot)<0);
                do{j--;} while(j!=left && arr[j].compareTo(pivot)>0);
                if(i<j) {Swap(arr,i,j);}
            }while(i<j);
            Swap(arr,left,j);
            quicksort(arr, left,j-1);
            quicksort(arr, j+1, right);
        }
    }
}
