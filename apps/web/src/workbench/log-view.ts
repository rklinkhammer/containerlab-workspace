// Presentation only: the backend still retrieves a bounded 100-line tail.
export function logView(text:string,tail:number,query:string){
 const lines=text===''?[]:text.replace(/\n$/,'').split('\n');
 const window=lines.slice(-([25,50,100].includes(tail)?tail:100));
 const needle=query.slice(0,256).toLowerCase();
 const matches=needle?window.filter(line=>line.toLowerCase().includes(needle)):window;
 return {text:matches.join('\n'),fetched:lines.length,window:window.length,matched:matches.length};
}
