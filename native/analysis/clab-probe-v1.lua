-- Reviewed synthetic protocol fixture, not application-health interpretation.
-- UDP/49321: ASCII CLAB, version 1, unsigned big-endian 16-bit sequence.
local p = Proto("clabprobe", "Reviewed CLAB probe")
local version = ProtoField.uint8("clabprobe.version", "Version", base.DEC)
local sequence = ProtoField.uint16("clabprobe.sequence", "Sequence", base.DEC)
p.fields = {version, sequence}
function p.dissector(buf, info, tree)
    if buf:len() ~= 7 then return 0 end
    if buf(0,4):string() ~= "CLAB" or buf(4,1):uint() ~= 1 then return 0 end
    info.cols.protocol = "CLABPROBE"
    local t = tree:add(p, buf())
    t:add(version, buf(4,1))
    t:add(sequence, buf(5,2))
    return 7
end
DissectorTable.get("udp.port"):add(49321, p)
