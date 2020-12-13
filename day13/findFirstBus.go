package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	fptr := flag.String("fpath", "schedule.txt", "schedule used")
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
	input.Scan()
	time, _ := strconv.Atoi(input.Text())
	input.Scan()
	options := input.Text()
	b := strings.Split(options, ",")
	bIDs := make([]int, 0, len(b))
	for _, bus := range b {
		num, err := strconv.Atoi(bus)
		if err != nil {
			continue
		}
		bIDs = append(bIDs, num)
	}
	part1(time, bIDs)
}

func part1(depart int, busIds []int) {
	waitTimes := make(map[int]int, len(busIds))
	for _, b := range busIds {
		waitTimes[b] = b - (depart % b)
	}
	small := math.MaxUint32
	var ans int
	for k, v := range waitTimes {
		if v < small {
			small = v
			ans = k * v
		}
	}
	fmt.Printf("Part 1 Ans: %d\n", ans)
}

func part2(buses []string) {
	first, _ := strconv.ParseInt(buses[0], 10, 64)
	areFound := false
	start := first
	for !areFound {

	}
}
