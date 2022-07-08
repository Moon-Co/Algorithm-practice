package DPPractice2;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int[] arr = new int[1000001];
        arr[2] = 1;
        arr[3] = 1;
        for(int i = 4;i <a+1;i++){
            if(i%3==0 && i%2 ==0){
                arr[i] = Math.min(1+arr[i/3],1+arr[i/2]);
                arr[i] = Math.min(arr[i],1+arr[i-1]);
            }
            else if(i%3==0){
                arr[i] = Math.min(1+arr[i/3],1+arr[i-1]);
            }
            else if(i%2 ==0){
                arr[i] = Math.min(1+arr[i/2],1+arr[i-1]);
            }
            else{
                arr[i] = 1+arr[i-1];
            }
            }
        System.out.println(arr[a]);
        }

}


