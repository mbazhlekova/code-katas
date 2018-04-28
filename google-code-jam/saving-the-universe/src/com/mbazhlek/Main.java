package com.mbazhlek;

import java.io.File;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
	    Scanner scanner = new Scanner(new File("input.in"));
	    PrintWriter output = new PrintWriter(new File("output.out"));

	    int token = scanner.nextInt(), size, queries, count;
	    String temp;

	    HashSet<String> set = new HashSet<String>();

	    scanner.nextLine();

	    for (int i = 1; i <= token; i++) {
	        set.clear();
	        count = 0;
	        size = scanner.nextInt();

	        for (int j = 0; j <= size; j++)
	            scanner.nextLine();


            queries = scanner.nextInt();
	        scanner.nextLine();

	        for (int k = 0; k < queries; k++) {
	            set.add(temp = scanner.nextLine());
	            if (set.size() == size) {
	                count++;
	                set.clear();
	                set.add(temp);
                }
            }
            output.println("Case #" + i + ": " + count);
        }
        scanner.close();
	    output.close();
    }
}
