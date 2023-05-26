import java.util.Scanner;
import java.lang.reflect.Array;

public class Stack {
    int SIZE;
    int[] stack;

    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        // System.out.println("ARRAY SIZE: ");
        // int N = sc.nextInt();
        // System.out.println(N + "\n");
        // int[] stack = new int[N];
        // for (int i = 0; i < N; i++) {
        // stack[i] = sc.nextInt();
        // }
        // print_all(stack, N);
        // sc.close();
        int[] array = { 534, 123, 453, 132, 12, 3 };
        Stack obj = new Stack();
        obj.SIZE = Array.getLength(array);
        obj.stack = array;
        print_all(obj.stack, obj.SIZE);

    }

    public boolean isempty(int[] stack, int N) {
        int size = Array.getLength(stack);
        if (N == size) {
            return false;
        }
        return true;
    }

    public static void print_all(int[] stack, int LEN) {
        System.out.print("[");
        for (int i = 0; i < LEN; i++) {
            System.out.print(stack[i]);
            System.out.print(", ");
        }
        System.out.print("]");

    }

}