module process (
    input rst,
    input clk,
    input [63:0] tim,
    input [63:0] dist,
    output  reg [31:0] res,
    output reg fin
);

integer counter;
integer total;
reg [63:0] lasttim;

always @(posedge clk) begin
    if (rst == 0) begin
        counter <=0;
        total <= 0;
        lasttim <= 0;
        res <= 0;
    end else if (tim != lasttim) begin
        if (counter == tim) begin
            lasttim <= tim;
            fin <= 1;
            counter <= 0;
            total<= 0;
            res <= total;
        end else begin
            // if calc with tim > dist then add one to total
            if (counter * (tim - counter) > dist) begin
                total <= total + 1;
            end
            counter <= counter + 1;
            fin <=0;
        end
        
    end
end

endmodule