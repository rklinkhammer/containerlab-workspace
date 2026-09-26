import {captureRequest,type CaptureResult,type ReanalysisResult} from '../../contracts/capture.ts';
const fields=captureRequest.pick({filename:true,duration:true,snaplen:true,captureFilter:true,displayFilter:true});
const hints:Record<string,string>={filename:'Use a filename ending in .pcap with letters, numbers, dots, dashes or underscores; no directory path.',duration:'Duration must be a whole number from 1 to 10 seconds.',snaplen:'Snapshot length must be a whole number from 64 to 65535 bytes.',captureFilter:'Capture filter must be at most 1024 characters with no control characters.',displayFilter:'Display filter must be at most 1024 characters with no control characters.'};
export function captureFormErrors(input:unknown):Record<string,string>{const x=fields.safeParse(input);if(x.success)return{};return Object.fromEntries(x.error.issues.map(i=>[String(i.path[0]),hints[String(i.path[0])]??'Check this setting.']));}
export function captureFeedback(result:CaptureResult,analysis:ReanalysisResult|null,now:number){
 const shown=analysis??result,remaining=Math.max(0,Math.ceil((Date.parse(result.expiresAt)-now)/1000));
 return {remaining,retention:remaining?`Save within ${remaining} seconds. The server then discards this artifact.`:'Artifact expired. Start a new capture to download or reanalyze.',
 limit:result.limited?'Capture marked size-limited. This file is a bounded sample; it does not contain all traffic.':null,
 analysis:shown.analysis==='filter_rejected'?'Display filter rejected. The original PCAP is retained; correct the filter and reanalyze.':shown.analysis==='unavailable'?'Packet analysis unavailable. The original PCAP is retained.':result.bytes===24?'No packets were captured in this file. This does not prove the link is idle.':!shown.packets.length?'No packets matched this display filter. The PCAP still contains captured data.':`Analysis finished · showing ${shown.packets.length} packet rows (maximum 100). This is not a total packet count.`};
}
