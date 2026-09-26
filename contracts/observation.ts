import{parseMultiObservation as parseLegacyMulti,type MultiObservation as LegacyMulti}from'./legacy/multi-observation.ts';
export * from './observation-history.ts';
import{parseInterfaceObservation,stateObservationSchema,profileObservationSchema,type InterfaceObservation,type StateObservation,type ProfileObservation}from'./observation-history.ts';
import{parseMultiObservation,type MultiObservation}from'./multi-observation.ts';
export function parseCurrentObservation(x:unknown):StateObservation|InterfaceObservation|ProfileObservation|MultiObservation|LegacyMulti{
 if(['observation/0.5','observation/0.6','observation/0.7','observation/0.8'].includes((x as any)?.contract))return parseLegacyMulti(x);
 if((x as any)?.contract==='observation/0.9')return parseMultiObservation(x);
 if((x as any)?.contract==='observation/0.4')return profileObservationSchema.parse(x);
 return (x as any)?.contract==='observation/0.2'?parseInterfaceObservation(x):stateObservationSchema.parse(x);
}
