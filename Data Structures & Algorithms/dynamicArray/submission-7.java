class DynamicArray {
    private int[] da;
    private int size;
    private int capacity;

    public DynamicArray(int capacity) {
        this.size = 0;
        this.capacity = capacity;
        this.da = new int[this.capacity];
    }

    public int get(int i) {
        return da[i];
    }

    public void set(int i, int n) {
        da[i] = n;
    }

    public void pushback(int n) {
        
        if(size == capacity){
            resize();
        }

        da[size] = n;
        size++;

    }

    public int popback() {
        if(size > 0){
            size --;
        }
        return da[size];
    }

    private void resize() {
        capacity *= 2;
        int[] new_da= new int [capacity];

        for(int i = 0; i < size; i++){
            new_da[i] = da[i];
        }

        da = new_da;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {

        return capacity;
    }
}
