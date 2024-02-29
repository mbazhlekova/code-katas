package main

import "fmt"

type MinStack struct {
	vals []int
	mins []int
}

func Constructor() MinStack {
	return MinStack{
		vals: []int{},
		mins: []int{},
	}
}

func (this *MinStack) Push(val int) {
	var minVal int
	if len(this.mins) == 0 {
		this.mins = append(this.mins, val)
	} else {
		minVal = min(val, this.mins[len(this.mins)-1])
		this.mins = append(this.mins, minVal)
	}

	this.vals = append(this.vals, val)
}

func (this *MinStack) Pop() {
	this.vals = this.vals[:len(this.vals)-1]
	this.mins = this.mins[:len(this.mins)-1]
}

func (this *MinStack) Top() int {
	return this.vals[len(this.vals)-1]
}

func (this *MinStack) GetMin() int {
	return this.mins[len(this.mins)-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
func main() {
	obj := Constructor()
	obj.Push(-1)
	obj.Push(0)
	obj.Push(-2)
	obj.Pop()
	obj.Top()
	obj.GetMin()

	fmt.Println(obj.vals)
	fmt.Println(obj.mins)
}
