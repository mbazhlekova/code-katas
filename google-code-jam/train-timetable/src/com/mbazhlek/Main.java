package com.mbazhlek;

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    private static int convertToMinutes(String time) {
        int timeInMinutes = 0;
        timeInMinutes += 60 * Integer.parseInt(time.substring(0, 2));
        timeInMinutes += Integer.parseInt(time.substring(3, 5));
        return timeInMinutes;
    }

    private static void setEvent(int eventType, int eventTime, ArrayList<Integer> events, ArrayList<Integer> eventTimes) {
        if (eventTime >= 1440) {
            return;
        }
        int index = 0;
        if (eventTimes.size() != 0) {
            while ((eventTimes.size() > index) && eventTimes.get(index) <= eventTime) {
                if (eventTimes.get(index) == eventTime) {
                    if ((eventType != 4 && eventType != 8) || (events.get(index) != 1 && events.get(index) != 2)) {
                        index++;

                    } else
                        break;
                } else
                    index++;
            }
        }
        eventTimes.add(index, eventTime);
        events.add(index, eventType);
    }

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(new File("input.in"));
        PrintWriter output = new PrintWriter(new File("output.out"));

        int numOfTestCases = scanner.nextInt(), turnaroundTime, tripsAtoB, tripsBtoA;
        ArrayList<Integer> events = new ArrayList<>();
        ArrayList<Integer> eventTimes = new ArrayList<>();

        for (int i = 1; i <= numOfTestCases; i++) {
            events.clear();
            eventTimes.clear();

            turnaroundTime = scanner.nextInt();
            tripsAtoB = scanner.nextInt();
            tripsBtoA = scanner.nextInt();

            for (int j = 0; j < tripsAtoB; j++) {
                setEvent(2, convertToMinutes(scanner.next()), events, eventTimes);
                setEvent(4, turnaroundTime + convertToMinutes(scanner.next()), events, eventTimes);
            }

            for (int k = 0; k < tripsBtoA; k++) {
                setEvent(1, convertToMinutes(scanner.next()), events, eventTimes);
                setEvent(8, turnaroundTime + convertToMinutes(scanner.next()), events, eventTimes);
            }
            tripsAtoB = 0;
            tripsBtoA = 0;
            int returnTripsAtoB = 0;
            int returnTripsBtoA = 0;
            for (int m = 0; m < events.size(); m++) {
                if ((events.get(m) & 8) > 0) {
                    tripsAtoB++;
                }
                if ((events.get(m) & 4) > 0) {
                    tripsBtoA++;
                }
                if ((events.get(m) & 2) > 0) {
                    tripsAtoB--;
                }
                if ((events.get(m) & 1) > 0) {
                    tripsBtoA--;
                }
                if (tripsAtoB == -1) {
                    tripsAtoB++;
                    returnTripsAtoB++;
                }
                if (tripsBtoA == -1) {
                    tripsBtoA++;
                    returnTripsBtoA++;
                }
            }
            output.println("Case # " + i + ": " + returnTripsAtoB + " " + returnTripsBtoA);
        }
        scanner.close();
        output.close();
    }
}
