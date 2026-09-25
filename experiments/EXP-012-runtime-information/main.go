// Disposable T2 probe. Native semantics remain exclusively in pinned Containerlab.
package main
import("bytes";"context";"encoding/json";"os";"time";"github.com/srl-labs/containerlab/core";rt "github.com/srl-labs/containerlab/runtime")
func main(){
 out:=map[string]any{"status":"rejected"};defer func(){if recover()!=nil{out=map[string]any{"status":"panic"}};json.NewEncoder(os.Stdout).Encode(out)}()
 c,err:=core.NewContainerLab(core.WithRuntime("docker",&rt.RuntimeConfig{Timeout:5*time.Second}),core.WithTopoPath(os.Args[1],nil));if err!=nil{out["stage"]="load";return}
 if err=c.ResolveLinks();err!=nil{out["stage"]="links";return}
 out["status"]="resolved";ns:=map[string]any{};for k,n:=range c.Nodes{cfg:=n.Config();ns[k]=map[string]any{"kind":cfg.Kind,"fixture_role":cfg.Labels["fixture-role"]}}
 out["nodes"]=ns;ls:=map[int]any{};for k,l:=range c.Links{es:=[]any{};for _,e:=range l.GetEndpoints(){es=append(es,map[string]any{"node":e.GetNode().GetShortName(),"interface":e.GetIfaceName(),"alias":e.GetIfaceAlias(),"display":e.GetIfaceDisplayName()})};ls[k]=map[string]any{"type":l.GetType(),"mtu":l.GetMTU(),"endpoints":es}}
 out["links"]=ls;exports:=map[string]any{};for _,mode:=range []string{"","__full","/missing-template"}{var b bytes.Buffer;err=c.GenerateExports(context.Background(),&b,mode);var obj map[string]any;decode:=json.Unmarshal(b.Bytes(),&obj);_,nodes:=obj["nodes"];_,links:=obj["links"];exports[mode]=map[string]any{"error":err!=nil,"valid_json":decode==nil,"nodes_present":nodes,"links_present":links,"bytes":b.Len(),"node_count":count(obj["nodes"]),"link_count":count(obj["links"])}}
 out["exports"]=exports
}

func count(v any) int {switch x:=v.(type){case map[string]any:return len(x);case []any:return len(x);default:return -1}}
