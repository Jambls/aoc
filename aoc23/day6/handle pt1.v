`include "process.v"
module handle;

integer fd;
integer code;
// these should be ints reg [8*8:1]
integer times [3:0];
integer distances [3:0];
integer results [3:0];
integer i;

reg clk;
initial clk = 0;
always
    #10 clk =~clk;

reg [31:0] tim;
reg [31:0] dist;
wire [31:0] res;
wire fin;
reg rst;

process u0 (
    .rst(rst),
    .clk(clk),
    .tim(tim),
    .dist(dist),
    .res(res),
    .fin(fin)
);

initial begin
    $dumpfile("test.vcd");
    $dumpvars(0,tim,dist,res,fin,results[0],clk);
    rst = 0;
    #40;
    rst = 1;
    fd = $fopen("input.txt", "r");
    code = $fscanf(fd, "%*s %d %d %d %d", times[0], times[1], times[2], times[3]);
    code = $fscanf(fd, "%*s %d %d %d %d", distances[0], distances[1], distances[2], distances[3]);
    
    for (i = 0; i < 4; i += 1) begin
        #20;
        tim = times[i];
        dist = distances[i];
        @(posedge fin);
        results[i] = res;
        # 20;
    end

        

    $display("times: %d, %d, %d", times[0], times [1], times[2]);
    $display("distances: %d, %d, %d", distances[0], distances [1], distances[2]);
    $display("results: %d, %d, %d, %d", results[0], results[1], results[2], results[3]);
    $display("result : %d", results[0] * results[1] * results[2] * results[3]);



    $fclose(fd);
    $finish;
end
endmodule