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

reg [63:0] tim;
reg [63:0] dist;
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
    $dumpvars(0,tim,dist,res,fin,results[0],clk, u0);
    rst = 0;
    #40;
    rst = 1;
    fd = $fopen("input.txt", "r");
    code = $fscanf(fd, "%*s %d %d %d %d", times[0], times[1], times[2], times[3]);
    code = $fscanf(fd, "%*s %d %d %d %d", distances[0], distances[1], distances[2], distances[3]);
    
    tim = 0;
    for (i = 0; i < 4; i += 1) begin
        tim = (tim * 100) + times[i];
    end
    dist = 0;
    for (i = 0; i < 4; i += 1) begin
        dist = (dist * 10000) + distances[i];
        $display("%d", dist);
    end

    $display("times: %d, %d, %d, %d", times[0], times [1], times[2], times[3]);
    $display("distances: %d, %d, %d, %d", distances[0], distances [1], distances[2], distances[3]);
    $display("tim : %d", tim);
    $display("dist : %d", dist);


    rst = 1;
    #20;
    @(posedge fin);
    results[i] = res;
    # 20;
    

        


    $display("results: %d, %d, %d, %d", results[0], results[1], results[2], results[3]);
    $display("result : %d", res);



    $fclose(fd);
    $finish;
end
endmodule