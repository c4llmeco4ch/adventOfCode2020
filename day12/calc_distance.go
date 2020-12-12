package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

func main() {
	fptr := flag.String("fpath", "directions.txt", "list of directions")
	part1(fptr)
	part2(fptr)
}

func part1(fptr *string) {
	flag.Parse()
	f, err := os.Open(*fptr)
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err = f.Close(); err != nil {
			log.Fatal(err)
		}
	}()
	input := bufio.NewScanner(f)
	shipX, shipY := 0, 0
	shipDirection := 0
	for input.Scan() {
		line := input.Text()
		command := line[:1]
		amount, _ := strconv.Atoi(line[1:])
		switch command {
		case "N":
			shipY += amount
		case "S":
			shipY -= amount
		case "E":
			shipX += amount
		case "W":
			shipX -= amount
		case "R":
			shipDirection = (shipDirection - amount) % 360
			for shipDirection < 0 {
				shipDirection += 360
			}
			shipDirection %= 360
		case "L":
			shipDirection = (shipDirection + amount)
			for shipDirection < 0 {
				shipDirection += 360
			}
			shipDirection %= 360
		case "F":
			if shipDirection == 0 {
				shipX += amount
			} else if shipDirection == 90 {
				shipY += amount
			} else if shipDirection == 180 {
				shipX -= amount
			} else {
				shipY -= amount
			}
		default:
			fmt.Printf("Uh oh...")
		}
	}
	fmt.Printf("The sum is %d\n", int(math.Abs(float64(shipX))+math.Abs(float64(shipY))))
}

func part2(fptr *string) {
	flag.Parse()
	f, err := os.Open(*fptr)
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err = f.Close(); err != nil {
			log.Fatal(err)
		}
	}()
	input := bufio.NewScanner(f)
	shipX, shipY := 0, 0
	waypointX, waypointY := 10, 1
	for input.Scan() {
		line := input.Text()
		command := line[:1]
		amount, _ := strconv.Atoi(line[1:])
		switch command {
		case "N":
			waypointY += amount
		case "S":
			waypointY -= amount
		case "E":
			waypointX += amount
		case "W":
			waypointX -= amount
		case "R":
			waypointX, waypointY = rotate(waypointX, waypointY, amount, true)
		case "L":
			waypointX, waypointY = rotate(waypointX, waypointY, amount, false)
		case "F":
			for i := 0; i < amount; i++ {
				shipX += waypointX
				shipY += waypointY
			}
		default:
			fmt.Printf("Uh oh...")
		}
	}
	fmt.Printf("The sum is %d\n", int(math.Abs(float64(shipX))+math.Abs(float64(shipY))))
}

func rotate(x, y, deg int, clockwise bool) (int, int) {
	for i := 0; i < int(math.Abs(float64(deg)))/90; i++ {
		tmpX, tmpY := y, x
		if x >= 0 && y >= 0 {
			if clockwise {
				tmpY *= -1
			} else {
				tmpX *= -1
			}
		} else if x >= 0 && y < 0 {
			if clockwise {
				tmpY *= -1
			} else {
				tmpX *= -1
			}
		} else if x < 0 && y >= 0 {
			if clockwise {
				tmpY *= -1
			} else {
				tmpX *= -1
			}
		} else {
			if clockwise {
				tmpY *= -1
			} else {
				tmpX *= -1
			}
		}
		x, y = tmpX, tmpY
	}
	return x, y
}
