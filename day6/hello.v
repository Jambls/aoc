module hello;

integer fd;
// this should be a string
integer str [64:1];
integer strptr;
// these should be ints reg [8*8:1]
integer times [3:0];
integer distances [3:0];
integer results [3:0];
integer i;

initial begin
    fd = $fopen("inputsmall.txt", "r");
    $fgets(str, fd);
    strptr = 0;

    while(str[strptr] < 48 || str[strptr] > 57) begin
        strptr +=1;
    end
    while(str[strptr] != 10) begin
        i = 0;
        while(str[strptr] >= 48 && str[strptr] <= 57) begin
            times[i] = times[i] *10 + str[strptr] - 48;
            strptr += 1;
            i += 1;
        end
    end

    $display("%d", times[2]);

    $fclose(fd);
    $display("Hello, World");
    $finish ;
end
endmodule